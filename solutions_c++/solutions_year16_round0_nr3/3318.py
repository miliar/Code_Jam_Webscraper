#include <functional>
#include <algorithm>
#include <iostream>
#include <climits>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <numeric>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <list>
#include <set>
#include <map>
#include <sstream>
#include <ostream>
#include <complex> 
#include <cstdarg>
#include <bitset> 
using namespace std;


typedef long long               LL;
typedef pair<int, int>          pii;
typedef pair<int, pii>          piii;
typedef vector<int>             vi;
typedef vector<pii>             vpii;
typedef vector<piii>            vpiii;
typedef vector<int>::iterator   vit;
typedef vector<LL> vll;
typedef long double				LD;

inline int sqr(int x) { return x * x; }
inline int cube(int x) { return x * x * x; }
inline LL sqrLL(LL x) { return x * x; }
inline LL cubeLL(LL x) { return x * x * x; }

const LL LLINF = 9223372036854775807LL;
const LL LLINF17 = 100000000000000000LL;
const int INF = 2147483647;
const int INF9 = 1000000000;
const LL MOD = 1000000007;
const double eps = 1e-7;
const double PI = acos(-1.0);

#define FOR(a,b,c)   for (int (a)=(b); (a)<(c); (a)++)
#define FORN(a,b,c)  for (int (a)=(b); (a)<=(c); (a)++)
#define FORD(a,b,c)  for (int (a)=(b); (a)>=(c); (a)--)
#define REP(i,n)     FOR(i,0,n)
#define REPN(i,n)    FORN(i,1,n)
#define REPD(i,n)    FORD(i,n,1)
#define rea(a,b)     read(a),read(b)
#define rean(a,b,c)  rea((a,b),c)
#define si(n)        scanf("%d", &n);
#define sil(n)       scanf("%I64d", &n);
#define pf(n)        printf("%d\n", n);
#define pl(n)        printf("%I64d\n",n);

#define RESET(a,b)   memset(a,b,sizeof(a)) 
#define SYNC         ios_base::sync_with_stdio(0);
#define SIZE(a)      (int)(a.size())
#define MIN(a,b)     (a) = min((a),(b))
#define MAX(a,b)     (a) = max((a),(b))
#define ALL(a)       a.begin(),a.end()
#define RALL(a)      a.rbegin(),a.rend()
#define SIZE(a)      (int)(a.size())
#define LEN(a)       (int)(a.length())
#define tr(container,it)   for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define fi           first
#define se           second
#define pp           push_back
#define mp           make_pair
#define ll           long long
#define gc           getchar_unlocked
#define deb(x )		cerr << #x << " here "<< x; 

#ifdef _WIN32
#define getchar_unlocked getchar
#define scanf            scanf_s
#endif

template<typename T > void check(T & a, const T & b) { if (a >= b) { a %= b; } }
template<typename T>void read(T &x) { register T c = gc(); x = 0; int t = 0; if (c == '-') t = 1, c = gc(); for (; (c < 48 || c>57); c = gc()); for (; c > 47 && c < 58; c = gc()) { x = (x << 1) + (x << 3) + c - 48; }if (t) x = -x; }
template<typename T>T gcd(T u, T v) {
	// simple cases (termination)
	if (u == v)
		return u;
	if (u == 0)
		return v;
	if (v == 0)
		return u;
	// look for factors of 2
	if (~u & 1) // u is even
	{
		if (v & 1) // v is odd
			return gcd(u >> 1, v);
		else // both u and v are even
			return gcd(u >> 1, v >> 1) << 1;
	}
	if (~v & 1) // u is odd, v is even
		return gcd(u, v >> 1);
	// reduce larger argument
	if (u > v)
		return gcd((u - v) >> 1, v);
	return gcd((v - u) >> 1, u);
}
LL mulmod(LL a, LL b, LL m) { LL q = (LL)(((LD)a*(LD)b) / (LD)m); LL r = a*b - q*m; if (r>m)r %= m; if (r<0)r += m; return r; }
//LL  expo(T e, T n) { T x = 1, p = e; while (n) { if (n & 1)x = x*p; p = p*p; n >>= 1; }return x; }
template <typename T>T power(T e, T n, T & m) { T x = 1, p = e; while (n) { if (n & 1)x = mod(x*p, m); p = mod(p*p, m); n >>= 1; }return x; }
template <typename T>T powerL(T e, T n, T & m) { T x = 1, p = e; while (n) { if (n & 1)x = mulmod(x, p, m); p = mulmod(p, p, m); n >>= 1; }return x; }
template <typename T> T InverseEuler(T a, T & m) { return (a == 1 ? 1 : power(a, m - 2, m)); }
LL _N;
ll expo(LL base, LL exp) {
	ll res = 1;
	while (exp>0) {
		if (exp % 2 == 1) res = (res*base);
		base = (base*base);
		exp /= 2;
	}
	return res;
}

/*int main() {
	SYNC; 
	int t;
	read(t);
	int x = 1;
	while (t--) {
		LL k, c, s;
		rea(k, c); read(s); 
		if (s == k) {
			cout << "Case #" << x++ << ": ";
			REPN(i, k) {
				printf("%d ", i);
			}
			cout << endl;
			continue; 
		}
		if (k == 2) {
			cout << "Case #" << x++ << ": " << 2 << endl; 
			continue; 
		}
		vi v; 
		v.pp(2); 
		v.pp(expo(k, c) - 1);

		if (k == 3) {
			if (c > 2 && s > 1) {
				cout << "Case #" << x++ << ": " << 2 << " " << 6 << endl;
			}
			else {
				cout << "Case #" << x++ << ": " << "IMPOSIBLE" << endl;
			}
			continue; 
		}

		if (k == 4) {
			if ( c > 2 && s > 1) cout << "Case #" << x++ << ": " << 2 << " " << expo(k,c) -1 << endl;
			else cout << "Case #" << x++ << ": " << "IMPOSIBLE" << endl;
			continue; 
		}
		if (k > 4) {

		}
	}

}*/

bool isPrime(LL n, vector<LL> & temp)
{

	if (n == 1)
		return false;
	else if (n<4)
		return true;
	else if (n % 2 == 0)
	{
		temp.pp(2);  return false;
	}
	else if (n<9)
		return true;
	else if (n % 3 == 0)
	{
		temp.pp(3); return false;
	}
	else
	{
		LL r = sqrt(n);
		LL f = 5;
		while (f <= r)
		{
			if (n%f == 0) { temp.pp(f); return false; }
			if (n % (f + 2) == 0) { temp.pp(f+2); return false; }
			f = f + 6;

		}
		return true;
	}
}

bool toBinary(LL n) {
	vll temp;
	LL s[64];
	int h = 0;
	while (n) {
		LL t = n % 2;
		s[h++] = t;
		n >>= 1;
	}
	for (LL i = 2; i <= 10; i++) {
		LL t = 0;
		for (LL j = 0; j <= _N-1; j++) {
			if (!j) {
				t += s[j]; 
				continue;
			}
			if (s[j]) {
				//cout << expo(i, j); 
				//cout << endl; 
				t += (expo(i, j)*s[j]);
			}
			//cout << t << endl; 
		}
		//cout << t << endl; 
		if (isPrime(t, temp)) {
			return 0;
		}
	}

	for (LL i = _N-1; i >= 0; i--) printf("%I64d", s[i]);
	printf(" ");
	for (LL i : temp) {
		printf("%I64d ", i); 
	}
	cout << endl; 
	return 1;
}

int main() {
	int t;
	read(t);
	while (t--) {
		 LL j; rea(_N, j);
		LL _t = 1 << (_N - 1);
		LL _a = 1 << (_N);
		//cout << _a << endl; 
		cout << "Case #1:" << endl; 
		for (LL i = _t + 1; i <= _a && j; i += 2) {
			if (toBinary(i)) {
				j--;
			}
		}
	}
	//cout << ans; 
	return 0; 
}