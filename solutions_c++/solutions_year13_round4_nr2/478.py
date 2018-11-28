#include<cstdio>
#include<cmath>
#include<cassert>
#include<cstring>
#include<ctime>
#include<iostream>
#include<fstream>
#include<sstream>
#include<algorithm>
#include<utility>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<deque>
#include<queue>
#include<stack>
#include<list>
#include<unordered_set>
#include<unordered_map>
using namespace std;
#define mp make_pair
#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define fi(i,n) for(size_t i=0;i<(n);++i)
#define fv(i,v) fi(i,(v).sz)
#define fit(i,v) for(auto i=v.begin();i!=v.end();++i)
#define frit(i,v) for(auto i=(v).rbegin();i!=(v).rend();++i)
#define fab(i,a,b) for(int i=(a);i<=(b);++i)
#define fba(i,b,a) for(int i=(b);i>=(a);--i)
#define INPC(t,x) t x;cin>>x
#define INP(x) INPC(int,x)
#define INP2(x,y) INP(x);INP(y)
#define INP3(x,y,z) INP2(x,y);INP(z)
#define INPS(x) INPC(string,x)
#define readArr(ptr,n) {fi(i,n)cin>>*((ptr)+i);}
#define readVec(v) readArr(v.begin(),(v).sz)
#define printArr(ptr,n) {fi(i,n)cout<<*((ptr)+i)<<(i==n-1?endl:' ');}
#define printVec(v) printArr(v.begin(),(v).sz)
#define uint unsigned int
#define uchar unsigned char
#define LL long long
#define uLL unsigned LL
#define V vector
#define VI vector<int>
#define VL vector<uLL>
#define VS vector<string>
#define P pair
uLL fact(uLL n,uLL m){return n?n*fact(n-1,m)%m:1;}
uLL gcd(uLL a,uLL b){return a?gcd(b%a,b):b;}
uLL lcm(uLL a,uLL b){return a/gcd(a,b)*b;}
uLL qpow(uLL a,uLL b,uLL m){return b?(b%2?b:1)*qpow(a*a%m,b/2,m)%m:1;}
bool isPow2(uLL x){return !(x&(x-1));}
void solve_the_problem();
int main() {
#ifdef _DEBUG
	freopen("input.txt","rt",stdin), freopen("output.txt","wt",stdout);	uLL t = clock();
#endif
	int tn;
	cin >> tn;
	for (int i = 0; i < tn; ++i) {
		cout << "Case #" << (i + 1) << ": ";
		solve_the_problem();
	}
#ifdef _DEBUG
	cerr << "Time: " << (double(clock() - t) / CLOCKS_PER_SEC) << endl;
#endif
	return 0;
}

uLL getWorst(uLL start, uLL total, uLL rounds) {
	uLL left = total - start - 1;
	uLL place = 0;
	for (uLL i = 0; i < rounds; ++i) {
		if (left == 0) {
			place += 1ULL << (rounds - i - 1);
		} else {
			left = (left - 1) / 2;
		}
	}
	return place;
}

uLL getBest(uLL start, uLL total, uLL rounds) {
	uLL left = start;
	uLL place = 0;
	for (uLL i = 0; i < rounds; ++i) {
		if (left != 0) {
			place += 1ULL << (rounds - i - 1);
			left = (left - 1) / 2;
		}
	}
	return place;
}

void solve_the_problem() {
	uLL n, p;
	cin >> n >> p;
	uLL l = 0, h = 1ULL << n;
	while (l < h - 1) {
		uLL m = (l + h) / 2;
		if (getWorst(m, 1ULL << n, n) < p) {
			l = m;
		} else {
			h = m;
		}
	}
	uLL w = l;
	l = 0, h = 1ULL << n;
	while (l < h - 1) {
		uLL m = (l + h) / 2;
		if (getBest(m, 1ULL << n, n) < p) {
			l = m;
		} else {
			h = m;
		}
	}
	uLL b = l;
	cout << b << " " << w << endl;
}
