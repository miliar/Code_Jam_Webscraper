#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
#define rep(i,n) for(int i=0;i<n;i++)
#define PI acos(-1.)

using namespace std;

template <typename T>
vector< complex<double> > fft (vector<T> a, bool inve = 0)
{
    int n = a.size();
    vector< complex<double> > res;
    if (n == 1) { 
            res.resize(1); 
            res[0] = complex<double>(a[0]);
            return res; 
        }
    complex<double> w(1, 0);
    complex<double> wn(cos(-2*PI/n), sin(-2*PI/n));
    if (inve) wn=complex<double>(cos(2*PI/n), sin(2*PI/n));
    vector< complex<double> > f0(n/2), f1(n/2);
    for(int i=0; i<n; i+=2)
        f0[i>>1] = a[i],
        f1[i>>1] = a[i+1];
    f0 = fft(f0, inve);
    f1 = fft(f1, inve);
    res.resize(n);
    for(int i=0; i<n/2; i++)
    {
        res[i] = f0[i] + w*f1[i];
        res[i+n/2] = f0[i] - w*f1[i];
        if (inve) res[i] /= 2, res[i+n/2] /= 2;
        w *= wn;
    }
    return res;
}

vector<int> multnum (vector<int> a, vector<int> b)
{
	reverse(a.begin(), a.end());
	reverse(b.begin(), b.end());
	int nn = max(a.size(), b.size());
    int n = 1;
    while (n < nn) n <<= 1;
    n <<= 1;
    a.resize(n);
    b.resize(n);
    vector< complex<double> > a1(a.begin(),a.end()),b1(b.begin(),b.end());
    vector<int> res(n);
    a1 = fft(a1, false);
    b1 = fft(b1, false);
    for(int i=0; i<n; i++) a1[i] = a1[i]*b1[i];
    a1 = fft(a1, true);
    for(int i=0; i<n; i++) res[i]=(int)(floor(a1[i].real()+0.1)+0.1);
    for(int i=0,carry=0;i<n || carry;i++)
    {
        if (i == n) { res.push_back(carry); break; }
        res[i]+=carry;
        carry = res[i]/10;
        res[i] %= 10;
    }
    while (res[res.size()-1]==0) res.erase(res.end()-1);
	reverse(res.begin(), res.end());
    return res;
}

vector<int> sumnum(vector<int> a, vector<int> b)
{
	int carry = 0;
	if (b.size()>a.size()) swap(a,b);
	vector<int> ret(a.size(), 0);
	rep(i,a.size())
	{
		if (i<b.size()) ret[ret.size() - 1 - i] = a[a.size() - 1 - i] + b[b.size() - 1 - i] + carry;
		else ret[ret.size() - 1 - i] = a[a.size() - 1 - i] + carry;
		carry = ret[ret.size() - 1 - i] / 10;
		ret[ret.size() - 1 - i] %= 10;
	}
	if (carry) ret.insert(ret.begin(), carry);
	//reverse(ret.begin(), ret.end());
	return ret;
}

vector<int> div2(vector<int> a)
{
	int carry = 0;
	vector<int> ret(a.size());
	rep(i,a.size())
	{
		carry = carry*10 + a[i];
		ret[i] = carry / 2;
		carry = carry - ret[i]*2;
	}
	if (ret[0]==0) ret.erase(ret.begin());
	return ret;
}

bool lesser(vector<int> a, vector<int> b)
{
	if (a.size()!=b.size()) return (a.size()<b.size());
	rep(i, a.size()) 
		if (a[i]<b[i]) return 1;
		else if (a[i]>b[i]) return 0;
	return 0;
}

bool bigger(vector<int> a, vector<int> b)
{
	if (a.size()!=b.size()) return (a.size()>b.size());
	rep(i, a.size()) 
		if (a[i]>b[i]) return 1;
		else if (a[i]<b[i]) return 0;
	return 0;
}

bool lessereq(vector<int> a, vector<int> b)
{
	if (a.size()!=b.size()) return (a.size()<b.size());
	rep(i, a.size()) 
		if (a[i]<b[i]) return 1;
		else if (a[i]>b[i]) return 0;
	return 1;
}

bool biggereq(vector<int> a, vector<int> b)
{
	if (a.size()!=b.size()) return (a.size()>b.size());
	rep(i, a.size()) 
		if (a[i]>b[i]) return 1;
		else if (a[i]<b[i]) return 0;
	return 1;
}


bool fllow = 0, flhigh = 0;

vector<int> serlow(vector<int> sqr)
{
	vector<int> left(1);
	left[0] = 1;
	vector<int> right(51);
	rep(i,right.size()) right[i] = 0;
	right[0] = 1;
	vector<int> lsqr = multnum(left, left);
	vector<int> rsqr = multnum(right, right);
	vector<int> cent;// = div2(sumnum(left, right);
	vector<int> csqr;// = multnum(cent, cent);
	while(left!=right)
	{
		/*rep(i, left.size()) cout << left[i];
		cout << " ";
		rep(i, right.size()) cout << right[i];
		cout << " ";*/
		cent = div2(sumnum(left, right));
		csqr = multnum(cent, cent);
		if (csqr==sqr) 
			{
				fllow = 1;
				return cent;
			}
		if (cent==right || cent==left) return left;
		//rep(i, cent.size()) cout << cent[i];
		//cout << "\n";
		
		if (lesser(csqr, sqr)) 
		{
			left = cent;
			lsqr = csqr;
		}
		else
		{
			right = cent;
			rsqr = csqr;
		}
	}
	return left;
}

vector<int> serhigh(vector<int> sqr)
{
	vector<int> left(1);
	left[0] = 1;
	vector<int> right(51);
	rep(i,right.size()) right[i] = 0;
	right[0] = 1;
	vector<int> lsqr = multnum(left, left);
	vector<int> rsqr = multnum(right, right);
	vector<int> cent;// = div2(sumnum(left, right);
	vector<int> csqr;// = multnum(cent, cent);
	while(left!=right)
	{
		cent = div2(sumnum(left, right));
		csqr = multnum(cent, cent);
		if (csqr==sqr) 
			{
				flhigh = 1;
				return cent;
			}
		if (cent==right || cent==left) return right;
		
		if (bigger(csqr, sqr)) 
		{
			right = cent;
			rsqr = csqr;
		}
		else
		{
			left = cent;
			lsqr = csqr;
		}
	}
	return left;
}

int T;

vector<long long> fsqr;

vector<int> digi;

vector<int> low, up;

vector<int> A, B;

unsigned long long ret = 0;

int ones = 0;

vector<int> cdigs;

void printnum(vector<int> &a)
{
	rep(i,a.size()) cout << a[i];
	cout << "\n";
}

vector< vector<int> > alldigs(0);

void processdig(int digi, int st)
{
	if (st==0) 
		{
			ones = 0;
			cdigs.resize(digi/2 + digi%2);
		}
	int cst = 0, cma = 1;
	if (st==0) { cst = 1; cma = 2; }
	if ((digi & 1) && st==digi/2)
	{
		if (digi>2)
		{
			cdigs[st] = 0;
			vector<int> tans(digi);
			rep(i, cdigs.size()) tans[i] = cdigs[i];
			rep(i, cdigs.size()-1) tans[tans.size()-1-i] = cdigs[i];
			//printnum(tans);
			/*if (lesser(tans, up) && bigger(tans, low)) ret++;
			else if (multnum(tans,tans)==A) ret++;
			else if (multnum(tans,tans)==B) ret++;*/
			alldigs.push_back(tans);
		}
		if (2*ones<9)
		{
			cdigs[st] = 1;
			vector<int> tans(digi);
			rep(i, cdigs.size()) tans[i] = cdigs[i];
			rep(i, cdigs.size()-1) tans[tans.size()-1-i] = cdigs[i];
			//printnum(tans);
			/*if (lesser(tans, up) && bigger(tans, low)) ret++;
			else if (multnum(tans,tans)==A) ret++;
			else if (multnum(tans,tans)==B) ret++;*/
			alldigs.push_back(tans);
		}
		if (2*ones<6)
		{
			cdigs[st] = 2;
			vector<int> tans(digi);
			rep(i, cdigs.size()) tans[i] = cdigs[i];
			rep(i, cdigs.size()-1) tans[tans.size()-1-i] = cdigs[i];
			//printnum(tans);
			/*if (lesser(tans, up) && bigger(tans, low)) ret++;
			else if (multnum(tans,tans)==A) ret++;
			else if (multnum(tans,tans)==B) ret++;*/
			alldigs.push_back(tans);
		}
		if (2*ones<1)
		{
			cdigs[st] = 3;
			vector<int> tans(digi);
			rep(i, cdigs.size()) tans[i] = cdigs[i];
			rep(i, cdigs.size()-1) tans[tans.size()-1-i] = cdigs[i];
			//printnum(tans);
			/*if (lesser(tans, up) && bigger(tans, low)) ret++;
			else if (multnum(tans,tans)==A) ret++;
			else if (multnum(tans,tans)==B) ret++;*/
			alldigs.push_back(tans);
		}
		return;
	}
	if (!(digi & 1) && st==(digi/2 - 1))
	{
		if (digi>2)
		{
			cdigs[st] = 0;
			vector<int> tans(digi);
			rep(i, cdigs.size()) tans[i] = cdigs[i];
			rep(i, cdigs.size()) tans[tans.size()-1-i] = cdigs[i];
			//printnum(tans);
			/*if (lesser(tans, up) && bigger(tans, low)) ret++;
			else if (multnum(tans,tans)==A) ret++;
			else if (multnum(tans,tans)==B) ret++;*/
			alldigs.push_back(tans);
		}
		if (2*ones<8)
		{
			cdigs[st] = 1;
			vector<int> tans(digi);
			rep(i, cdigs.size()) tans[i] = cdigs[i];
			rep(i, cdigs.size()) tans[tans.size()-1-i] = cdigs[i];
			//printnum(tans);
			/*if (lesser(tans, up) && bigger(tans, low)) ret++;
			else if (multnum(tans,tans)==A) ret++;
			else if (multnum(tans,tans)==B) ret++;*/
			alldigs.push_back(tans);
		}
		if (2*(ones+4)<10)
		{
			cdigs[st] = 2;
			vector<int> tans(digi);
			rep(i, cdigs.size()) tans[i] = cdigs[i];
			rep(i, cdigs.size()) tans[tans.size()-1-i] = cdigs[i];
			//printnum(tans);
			/*if (lesser(tans, up) && bigger(tans, low)) ret++;
			else if (multnum(tans,tans)==A) ret++;
			else if (multnum(tans,tans)==B) ret++;*/
			alldigs.push_back(tans);
		}
		return;
	}
	for(int i=cst;i<=cma;++i)
	{
		if (2*(ones+i*i)<10)
		{
			cdigs[st] = i;
			ones += i*i;
			processdig(digi, st + 1);
			ones -= i*i;
		}
	}
	return;
}


int main()
{
    fstream fin("C-large-2.in",ifstream::in);
    fstream fout("C-large-2.out",ofstream::out);
    fin >> T;
	for(int dig=1;dig<=50;++dig) 
	{
		processdig(dig, 0);
		cout << dig << " ";
	}
	cout << "\n";
	for(int tc=1;tc<=T;tc++)
    {
        if (tc%10==0) cout << tc << "\n";
		ret = 0;
		string AA, BB;
		fin >> AA >> BB;
		A.resize(AA.size());
		rep(i,A.size()) A[i] = AA[i] - '0';
		B.resize(BB.size());
		rep(i,B.size()) B[i] = BB[i] - '0';
		bool fl1 = 0, fl2 = 1;
		fllow = flhigh = 0;
		low = serlow(A);
		up = serhigh(B);
		rep(i,alldigs.size())
		{
			//if (i%100==0) cout << i << " " << alldigs.size() << "\t";
			if (!fl1) 
				{
					if (!fllow) fl1 = bigger(alldigs[i], low);//fl1 = bigger(multnum(alldigs[i], alldigs[i]), A);
					else fl1 = biggereq(alldigs[i], low);
				}
			if (!fl1) continue;
			if (fl2) 
				{
					if (!flhigh) fl2 = lesser(alldigs[i], up);
					else fl2 = lessereq(alldigs[i], up);
				}
			if (!fl2) break;
			if (fl1 && fl2) ret++;
		}
		fout << "Case #" << tc << ": " << ret << "\n";

    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC << "\n";
    system("PAUSE");
    return 0;
}
