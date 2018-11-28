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
typedef long double ld;
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
template<class T> int cntbit(T s) { return __builtin_popcount(s); }
const int bfsz = 1 << 16; char bf[bfsz + 5]; int rsz = 0;int ptr = 0;
char gc() { if (rsz <= 0) { ptr = 0; rsz = (int) fread(bf, 1, bfsz, stdin); if (rsz <= 0) return EOF; } --rsz; return bf[ptr++]; }
void ga(char &c) { c = EOF; while (!isalpha(c)) c = gc(); }
int gs(char s[]) { int l = 0; char c = gc(); while (isspace(c)) c = gc(); while (c != EOF && !isspace(c)) { s[l++] = c; c = gc(); } s[l] = '\0'; return l; }
template<class T> bool gi(T &v) {
    v = 0; char c = gc(); while (c != EOF && c != '-' && !isdigit(c)) c = gc(); if (c == EOF) return false; bool neg = c == '-'; if (neg) c = gc();
    while (isdigit(c)) { v = v * 10 + c - '0'; c = gc(); } if (neg) v = -v; return true;
}
typedef pair<int, int> II;
const ld PI = acos(-1.0);
const ld eps = 1e-9;
const int dr[] = { -1, 0, +1, 0};
const int dc[] = { 0, +1, 0, -1};
const int inf = (int) 1e9 + 5;
const ll linf = (ll) 1e16 + 5;

#define maxn 200005

int test, n;
ll b, a[40], x[40];
int A;

ld cal(ll x){
	ll num = 0, sum = 0;
	For(i, 1, A) {
		if(a[i] > x) return -1;
		num += (x - a[i]);
		sum += (x - a[i]);
	}
	For(i, A + 1, 37){
		sum += max(0ll, x + 1 - a[i]);
	}
	if(sum > b) return -1;
	return num * 36.0 / A - sum;
}

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
//	freopen("code.out", "w", stdout);

	cin >> test;
//	cout << test << endl;
	For(itest, 1, test){
		cin >> b >> n;
		ms(a, 0);
		For(i, 1, n) cin >> x[i];
		sort(x + 1, x + n + 1);
		For(i, 1, n) a[37 - n + i] = x[i];
		For(i, 2, 37) a[i] -= a[1];
		a[1] = 0;
		ld res = 0;
		for(A = 1; A <= 37; A++){
			ll l = 0, r = 1ll << 12, m1, m2;
			while(l < r - 3){
//				cout << A << " " << m1 << " " << m2 << endl;
				m1 = (l + l + r) / 3;
				m2 = (l + r + r) / 3;
				if(cal(m1) < cal(m2)){
					l = m1;
				}
				else r = m2;
			}
			For(i, l, r) res = max(res, cal(i));
		}
		cout << fixed << setprecision(9);
		cout << "Case #" << itest << ": " << res << endl;
	}

	return 0;

}
