#include <set>
#include <map>
#include <list>
#include <cmath>
#include <queue>
#include <stack>
#include <cstdio>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iomanip>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <ctime>
#include <deque>
#include <bitset>
#include <cctype>
#include <utility>
#include <cassert>

using namespace std;

typedef long long ll;
typedef double ld;
typedef unsigned int ui;
typedef unsigned long long ull;

#define Rep(i,n) for(int i = 0; i < (n); ++i)
#define Repd(i,n) for(int i = (n)-1; i >= 0; --i)
#define For(i,a,b) for(int i = (a); i <= (b); ++i)
#define Ford(i,a,b) for(int i = (a); i >= (b); --i)
#define Fit(i,v) for(__typeof((v).begin()) i = (v).begin(); i != (v).end(); ++i)
#define Fitd(i,v) for(__typeof((v).rbegin()) i = (v).rbegin(); i != (v).rend(); ++i)
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define sz(a) ((int)(a).size())
#define all(a) (a).begin(), (a).end()
#define ms(a,x) memset(a, x, sizeof(a))

template<class F, class T> T convert(F a, int p = -1) { stringstream ss; if (p >= 0) ss << fixed << setprecision(p); ss << a; T r; ss >> r; return r; }
template<class T> T gcd(T a, T b) { T r; while (b != 0) { r = a % b; a = b; b = r; } return a; }
template<class T> T lcm(T a, T b) { return a / gcd(a, b) * b; }
template<class T> T sqr(T x) { return x * x; }
template<class T> T cube(T x) { return x * x * x; }
template<class T> int getbit(T s, int i) { return (s >> i) & 1; }
template<class T> T onbit(T s, int i) { return s | (T(1) << i); }
template<class T> T offbit(T s, int i) { return s & (~(T(1) << i)); }
template<class T> int cntbit(T s) { return s == 0 ? 0 : cntbit(s >> 1) + (s & 1); }
const int bfsz = 1 << 16; char bf[bfsz + 5]; int rsz = 0;int ptr = 0;
char gc() { if (rsz <= 0) { ptr = 0; rsz = (int) fread(bf, 1, bfsz, stdin); if (rsz <= 0) return EOF; } --rsz; return bf[ptr++]; }
void ga(char &c) { c = EOF; while (!isalpha(c)) c = gc(); }
int gs(char s[]) { int l = 0; char c = gc(); while (isspace(c)) c = gc(); while (c != EOF && !isspace(c)) { s[l++] = c; c = gc(); } s[l] = '\0'; return l; }
template<class T> bool gi(T &v) {
    v = 0; char c = gc(); while (c != EOF && c != '-' && !isdigit(c)) c = gc(); if (c == EOF) return false; bool neg = c == '-'; if (neg) c = gc();
    while (isdigit(c)) { v = v * 10 + c - '0'; c = gc(); } if (neg) v = -v; return true;
}

typedef pair<int, int> II;

const double PI = acos(-1.0);
const double eps = 1e-9;

const int inf = (int)1e9 + 5;
const ll linf = (ll)1e17 + 5;
const ll mod = 1000002013;
#define maxn 2005

struct Ticket{
	int l, r, num;
	Ticket(int _l, int _r, int _num){
		l = _l; r = _r; num = _num;
	}
};

vector<int> V, flag;
int test, n, m, l, r, num;
ll x;
pair<ll, ll> a[maxn], b[maxn];

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> test;
	For(itest, 1, test){
		cin >> n >> m;
		ll res = 0;
		Rep(run, m){
			cin >> l >> r >> num;
			x = (r - l);
			x = (x * (x - 1) / 2) % mod;
			res = (res - x * num) % mod;
			a[run] = mp(l, num);
			b[run] = mp(r, num);
		}
//		cout << res << endl;

		sort(a, a + m); sort(b, b + m);
		Rep(i, m){
			Ford(j, m - 1, 0){
				if(b[i].fi >= a[j].fi){
					num = min(b[i].se, a[j].se);
					x = b[i].fi - a[j].fi;
					x = (x * (x - 1) / 2) % mod;
					res = (res + x * num) % mod;
					b[i].se -= num; a[j].se -= num;
				}
			}
		}
		res = (res + mod) % mod;
		cout << "Case #" << itest << ": " << res << endl;

	}

    return 0;
}
