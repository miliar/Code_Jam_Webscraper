#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <utility>
#include <numeric>
#include <fstream>

using namespace std;

#define		ALL(c)	(c).begin(),(c).end()
#define		SZ(c)	int((c).size())
#define		LEN(s)	int((s).length())
#define		FOR(i,n)	for(int i=0;i<(n);++i)
#define		FORD(i,a,b)	for(int i=(a);i<=(b);++i)
#define		FORR(i,a,b)	for(int i=(b);i>=(a);--i)

typedef istringstream iss;
typedef ostringstream oss;
typedef long double ld;
typedef long long i64;
typedef pair<int,int> pii;

typedef vector<i64> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;

typedef vector<ld> vd;
typedef vector<vd> vvd;

typedef vector<string> vs;

const i64 d18 = 1000000000000000000LL;
const ld eps = 1e-9;
const ld pi = atan2(0.0, -1.0);
template<class T> T sqr(T a) { return a * a; }
i64 abs(i64 a) { return (a >= 0) ? a : -a; }

ofstream LOG("log.txt");

ifstream fin;
ofstream fout;

#include <memory.h>

class bnum
{
public:
	static const int bnsize = 40;
	static const int dpc = 4;
	static const i64 dm = 10000;
	bnum() { n = 1; memset(a, 0, bnsize*sizeof(int)); }
	explicit bnum(i64 k)
	{
		memset(a, 0, bnsize*sizeof(int));
		if (k == 0)	
			n = 1;
		else
			for (n = 0; k > 0; k /= dm) a[n++] = (int)(k % dm); 
	}
	explicit bnum(string s)
	{
		memset(a, 0, bnsize*sizeof(int));
		if (s.empty()) 
			n = 1;
		else
		{
			int i = LEN(s);
			for (n = 0; i > dpc; i -= dpc) a[n++] = atoi(s.substr(i-dpc, dpc).c_str());
			a[n++] = atoi(s.substr(0, i).c_str());
		}
	}
	const bnum& operator+=(const bnum& b)
	{
		n = max(n, b.n);
		int ost = 0, i;
		for (i = 0; i < n || ost > 0; ++i)
		{
			a[i] += b.a[i] + ost;
			ost = a[i] / dm;
			if (a[i] >= dm) a[i] -= dm;
		}
		n = i;
		return *this;
	}
	const bnum& operator-=(const bnum& b)
	{
		if (*this < b) return (*this = bnum(0));
		n = max(n, b.n);
		int ost = 0;
		for (int i = 0; i < n || ost > 0; ++i)
		{
			a[i] -= b.a[i] + ost;
			if (a[i] < 0)
			{
				ost = 1;
				a[i] += dm;
			}
			else
				ost = 0;
		}
		while (n > 1 && a[n-1] == 0) --n;
		return *this;
	}
	const bnum& operator*=(const bnum& b)
	{
		if (n == 1 && a[0] == 0 || b.n == 1 && b.a[0] == 0) return (*this = bnum(0));
		bnum c(0);
		for (int i = 0; i < n; ++i)
		{
			int ost = 0, j;
			for (j = 0; j < b.n || ost; ++j)
			{
				c.a[i+j] += a[i] * b.a[j] + ost;
				ost = c.a[i+j] / dm;
				c.a[i+j] %= dm;
			}
			c.n = i + j;
		}
		return (*this = c);
	}
	// M <= 9 * 10^14
	const bnum& operator*=(i64 M)
	{
		i64 ost = 0;
		int i;
		for (i = 0; i < n || ost; ++i)
		{
			ost = a[i] * M + ost;
			a[i] = (int)(ost % dm);
			ost /= dm;
		}
		n = i;
		return *this;
	}
	// M <= 9 * 10^14
	const bnum& operator/=(i64 M)
	{
		i64 ost = 0;
		FORR(i, 0, n-1)
		{
			ost = ost * dm + a[i];
			a[i] = (int)(ost / M);
			ost %= M;
		}
		while (n > 1 && a[n-1] == 0) --n;
		return *this;
	}
	string to_str() const
	{
		oss ostr;
		ostr << a[n-1];
		FORR(i, 0, n-2)
			ostr << setw(4) << setfill('0') << a[i];
		return ostr.str();
	}
	int length() const
	{
		int res = (n-1) * 4 + 1;
		for (int d = 10; a[n-1] >= d; d *= 10) ++res;
		return res;
	}
	bool operator<(const bnum& b) const
	{
		if (n < b.n) return true;
		if (n > b.n) return false;
		FORR(i, 0, n-1) 
		{
			if (a[i] < b.a[i]) return true;
			if (a[i] > b.a[i]) return false;
		}
		return false;
	}
	bool operator==(const bnum& b) const
	{
		if (n != b.n) return false;
		FORR(i, 0, n-1) if (a[i] != b.a[i]) return false;
		return true;
	}
	bool operator<=(const bnum& b) const
	{
		return (*this < b || *this == b);
	}
	bool operator>(const bnum& b) const
	{
		return !(*this < b) && !(*this == b);
	}
	bool operator>=(const bnum& b) const
	{
		return !(*this < b);
	}
	bool operator!=(const bnum& b) const
	{
		return !(*this == b);
	}
private:
	int n;
	int a[bnsize];
	friend i64 operator%(const bnum& a, i64 M);
};

bnum operator+(const bnum& a, const bnum& b)
{
	return (bnum(a) += b);
}
bnum operator-(const bnum& a, const bnum& b)
{
	return (bnum(a) -= b);
}
bnum operator*(const bnum& a, const bnum& b)
{
	return (bnum(a) *= b);
}
// M <= 9 * 10^14
bnum operator*(const bnum& a, i64 M)
{
	return (bnum(a) *= M);
}
// M <= 9 * 10^14
bnum operator/(const bnum& a, i64 M)
{
	return (bnum(a) /= M);
}
// M <= 9 * 10^14
i64 operator%(const bnum& a, i64 M)
{
	i64 res = 0;
	FORR(i, 0, a.n-1) res = (res * bnum::dm + a.a[i]) % M;
	return res;
}

vector<bnum> Q;

int sbnext(int N)
{
	if (N == 0) return 1<<30;
	int m = N&-N;
	return (((N+m)^(N&(N+m)))/(m<<1)-1)|(N+m);
}

bool isPali(const string & s)
{
	for (int i = 0, j = LEN(s)-1; i < j; ++i, --j)
		if (s[i] != s[j])
			return false;
	return true;
}

void Preprocess()
{
	FORD(i, 1, 3) Q.push_back(bnum(i));
	FORD(len, 2, 50)
	{
		if (len % 2 == 0)
		{
			int p = len/2-1;
			for (int ones = 0; ones <= 3 && ones <= p; ++ones)
			{
				for (int msk = (1<<ones)-1; msk < 1<<p; msk = sbnext(msk))
				{
					string num(len, '0');
					num[0] = '1';
					FOR(i, p) if (msk & (1<<i)) num[p-i] = '1';
					FOR(i, p+1) num[len-1-i] = num[i];
					Q.push_back(bnum(num));
				}
			}
			string num(len, '0');
			num[0] = num[len-1] = '2';
			Q.push_back(bnum(num));
		}
		else
		{
			int p = len/2-1;
			for (int ones = 0; ones <= 3 && ones <= p; ++ones)
			{
				for (int msk = (1<<ones)-1; msk < 1<<p; msk = sbnext(msk))
				{
					string num(len, '0');
					num[0] = '1';
					FOR(i, p) if (msk & (1<<i)) num[p-i] = '1';
					FOR(i, p+1) num[len-1-i] = num[i];
					FORD(c, '0', '2')
					{
						num[len/2] = c;
						bnum bn(num);
						if (isPali((bn*bn).to_str()))
							Q.push_back(bn);						
					}
				}
			}
			string num(len, '0');
			num[0] = num[len-1] = '2';
			Q.push_back(bnum(num));
			num[len/2] = '1';
			Q.push_back(bnum(num));
		}
	}

	sort(ALL(Q));

	LOG << "Preprocess done\n";
	LOG << "Quantity " << SZ(Q) << endl;
	FOR(i, SZ(Q)) LOG << Q[i].to_str() << " " << (Q[i]*Q[i]).to_str() << endl;
	FOR(i, SZ(Q)) Q[i] *= Q[i];
}

void solve_case(int TN)
{
	string A, B;
	fin >> A >> B;
	int ans = (int)(upper_bound(ALL(Q), bnum(B)) - lower_bound(ALL(Q), bnum(A)));
	fout << "Case #" << TN << ": " << ans << endl;
	cout << "Case #" << TN << ": " << ans << endl;
}

int main()
{
	Preprocess();

	fin.open("C.in"); 
	fout.open("C.out");

	int T; 
	fin >> T;
	FOR(tt, T)
	{
		solve_case(tt+1);
	}

	return 0;	
}
