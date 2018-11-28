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
#define null		NULL

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
#define deb(x)		cerr << #x << " here "<< x; 

#ifdef _WIN32
#define getchar_unlocked getchar
#define scanf            scanf_s
#endif

template<typename T > void check(T & a, const T & b) { if (a >= b) { a %= b; } }
template<typename T>void read(T &x) { register T c = gc(); x = 0; int t = 0; if (c == '-') t = 1, c = gc(); for (; (c < 48 || c>57); c = gc()); for (; c > 47 && c < 58; c = gc()) { x = (x << 1) + (x << 3) + c - 48; }if (t) x = -x; }
/*template <typename T> void outPos(T n) { char snum[65]; int i = 0; do { snum[i++] = n % 10 + '0'; n /= 10; } while (n); i = i - 1; while (i >= 0)outchar(snum[i--]); outchar('\n'); }
*/template<typename T>T gcd(T u, T v) {
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
template < typename T > T mod(T x, T m) { if (x >= m)return x%m; else return x; }
LL mulmod(LL a, LL b, LL m) { LL q = (LL)(((LD)a*(LD)b) / (LD)m); LL r = a*b - q*m; if (r>m)r %= m; if (r<0)r += m; return r; }
template <typename T, typename S>T expo(T e, S n) { T x = 1, p = e; while (n) { if (n & 1)x = x*p; p = p*p; n >>= 1; }return x; }
template <typename T>T power(T e, T n, T  m) { T x = 1, p = e; while (n) { if (n & 1)x = mod(x*p, m); p = mod(p*p, m); n >>= 1; }return x; }
template <typename T>T powerL(T e, T n, T  m) { T x = 1, p = e; while (n) { if (n & 1)x = mulmod(x, p, m); p = mulmod(p, p, m); n >>= 1; }return x; }
template <typename T> T InverseEuler(T a, T  m) { return (a == 1 ? 1 : powerL(a, m - 2, m)); }
int main() {
	int t; 
	read(t); 
	int x = 1; 
	while (t--) {
		string s;
		cin >> s;
		cout << "Case #" << x++ << ": ";
		int a[26] = { 0 };
		int b[26] = { 0 }; 
		vi v; 
		for (int i = 0; i < s.size(); i++) {
			a[s[i] - 'A']++; 
			b[s[i] - 'A']++;
		}
		string _s[12] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
		int i = 9; 
		while ( i >= 0) {
			bool _t = 0; 
			//for (int t = 0; t < 26; t++) { cout << char(t + int('A')) << " " << a[t]; }
			for (int j = 0; j < _s[i].size(); j++) {
				if (a[_s[i][j] - 'A'] <= 0) { _t = 1; break; }
			}
			if (_t) { i--;}
			else {
				bool __t = 0; 
				for (int j = 0; j < _s[i].size(); j++) {
					a[_s[i][j] - 'A']--;
					if (a[_s[i][j]-'A'] < 0) {
						__t = 1; 
						for (int k = 0; k <= j; k++) {
							a[_s[i][k] - 'A']++; 
						}
						break;
					}
				}
				if (!__t) { v.pp(i); }
				else { i--;  }
			} 
			//for (int j = 0; j < 26; j++) { cout << char(j + int('A')) << " " << a[j] << " "; }
			//cout << endl;
		}
		i = 0; 
		int num = 1; 
		REP(t1, 26) {
			if (a[t1]) {
				num = 0; 
				vi ___t; 
				while (i < 10) {
					bool _t = 0;
					//for (int t = 0; t < 26; t++) { cout << char(t + int('A')) << " " << a[t]; }
					for (int j = 0; j < _s[i].size(); j++) {
						if (b[_s[i][j] - 'A'] <= 0) { _t = 1; break; }
					}
					if (_t) { i++; }
					else {
						bool __t = 0;
						for (int j = 0; j < _s[i].size(); j++) {
							b[_s[i][j] - 'A']--;
							if (b[_s[i][j] - 'A'] < 0) {
								__t = 1;
								for (int k = 0; k <= j; k++) {
									b[_s[i][k] - 'A']++;
								}
								break;
							}
						}
						if (!__t) { ___t.pp(i); }
						else { i++; }
					}
					//for (int j = 0; j < 26; j++) { cout << char(j + int('A')) << " " << a[j] << " "; }
					//cout << endl;
				}
				for (int al : ___t) { cout << al;  }
				break;
			}
		}
		sort(ALL(v));
		if (num) {
			REP(__T, v.size()) { cout << v[__T]; }
		}
		cout << endl; 
	}
	return 0;
}