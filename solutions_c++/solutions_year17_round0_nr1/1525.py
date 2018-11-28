#include<bits/stdc++.h>
#include <regex>
#include<ext/numeric>
#include<ext/hash_map>
using namespace std;
using namespace __gnu_cxx;

#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz(v)  (int)v.size()
#define WHITE -1
#define GREY   0
#define BLACK  1
#define CLR(a,v) memset(a,v,sizeof a)
#define PC(x) __builtin_popcount(x)
#define PCLL(x) __builtin_popcountll(x)
#define MP make_pair

typedef long long ll;
typedef pair<int, int> ii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<ll> vll;
//typedef unsigned int ui;

typedef complex<double> point;
//#define X real()
//#define Y imag()
#define vec(a,b) ((b)-(a))
#define dot(a,b) ((conj(a)*(b)).real())
#define cross(a,b) ((conj(a)*(b)).imag())
#define colliner pointOnLine
#define same(a,b) (lengthSqr(vec(a,b))<EPS)
#define lengthSqr(v) (dot(v,v))

const double PI = acos(-1.0);

int dx[] = { 0, -1, 0, 1, -1, -1, 1, 1 };
int dy[] = { 1, 0, -1, 0, 1, -1, 1, -1 };

int DX[] = { 1, 1, -1, -1, 2, 2, -2, -2 };
int DY[] = { 2, -2, 2, -2, 1, -1, 1, -1 };

const int MAX = 1005, MOD = 1e9 + 7, oo = (1 << 30), MAXN = 1e6 + 5;
const ll OO = 1ll << 60;
const double EPS = 1e-9;

int t, k, flip[MAX];
char s[MAX];

int main() {
#ifndef ONLINE_JUDGE
	freopen("IN.in", "r", stdin);
//	freopen("access.in", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	scanf("%d", &t);
	for (int T = 1; T <= t; ++T) {
		printf("Case #%d: ", T);
		CLR(flip, 0);
		scanf("%s", s);
		scanf("%d", &k);
		int n = strlen(s);
		int cur = 0, ans = 0;
		for (int i = 0; i < n - k; ++i) {
			cur -= flip[i];
			if ((s[i] == '-' && !(cur & 1)) || (s[i] == '+' && (cur & 1)))
				++flip[i + k], cur++, ans++;
		}
		bool tbf = 0, tnf = 0;
		for (int i = n - k; i < n; ++i) {
			cur -= flip[i];
			if ((s[i] == '-' && !(cur & 1)) || (s[i] == '+' && (cur & 1)))
				tbf = 1;
			else
				tnf = 1;
		}
		if (tbf ^ tnf) {
			ans += tbf;
			printf("%d\n", ans);
		} else
			puts("IMPOSSIBLE");
	}
}

