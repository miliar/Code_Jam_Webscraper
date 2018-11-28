#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <string>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <functional>
#include <queue>
#include <stack>
#include <cmath>
#include <iomanip>
#include <list>
#include <tuple>
#include <bitset>
#include <ciso646>
#include <cassert>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<ll, ll> P;
typedef tuple<ll, ll, ll> T;
typedef vector<ll> vec;

inline bool check(ll x, ll y, ll xMax, ll yMax) { return x >= 0 && y >= 0 && xMax > x && yMax > y; }
inline int toint(string s) { int v; istringstream sin(s); sin >> v; return v; }
template<class T> inline string tostring(T x) { ostringstream sout; sout << x; return sout.str(); }
template<class T> inline T sqr(T x) { return x*x; }
template<class T> inline T mypow(T x, ll n) { T res = 1; while (n > 0) { if (n & 1)res = res * x;	x = x * x;	n >>= 1; }return res; }
inline ll gcd(ll a, ll b) { return b ? gcd(b, a%b) : a; }
inline ll lcm(ll a, ll b) { return a / gcd(a, b) * b; }

#define For(i,a,b)	for(ll (i) = (a);i < (b);(i)++)
#define rep(i,n)	For(i,0,n)
#define rFor(i,a,b)	for(ll (i) = (a-1);i >= (b);(i)--)
#define rrep(i,n)	rFor(i,n,0)
#define each(i,n)	for(auto &i : n)
#define clr(a)		memset((a), 0 ,sizeof(a))
#define mclr(a)		memset((a), -1 ,sizeof(a))
#define all(a)		(a).begin(),(a).end()
#define sz(a)		(sizeof(a))
#define tostr(a)	tostring(a)
#define dump(val) 	cerr << #val " = " << val << endl;
#define Fill(a,v)	fill((int*)a,(int*)(a+(sz(a)/sz(*(a)))),v)

const ll dx[8] = { 1, 0, -1, 0, 1, 1, -1, -1 }, dy[8] = { 0, -1, 0, 1, -1, 1, -1, 1 };

const ll mod = 1e9 + 7;
const ll INF = 1e17 + 9;

#define int ll
#define double ld

signed main() {
	cin.tie(0);
	ios_base::sync_with_stdio(false);

	int T;
	cin >> T;

	for (int _ = 0; _ < T; _++) {
		cout << "Case #" << _ + 1 << ": ";
		int n;
		cin >> n;
		set<pair<int,char>, greater<pair<int,char>>> p;
		int sum = 0;
		for (int i = 0; i < n; i++) {
			pair<int, char> tmp;
			cin >> tmp.first;
			sum += tmp.first;
			tmp.second = 'A' + i;
			p.insert(tmp);
		}
		vector<string> ans(1,"");
		do {
			if (p.begin()->first == 0)break;
			auto tp = *p.begin();
			p.erase(tp);
			tp.first--;
			char tc = tp.second;
			p.insert(tp);
			sum--;
			if (ans.back().size() == 2) {
				ans.push_back("");
			}
			ans.back() += tc;
			if (p.begin()->first * 2 <= sum && (p.size() == 1 || next(p.begin())->first * 2 <= sum)) {
				ans.push_back("");
			}			
		} while (1);
		if (ans.back() == "")ans.pop_back();
		rep(i, ans.size()) {
			cout << ans[i];
			if (ans.size() - 1 != i) {
				cout << " ";
			}
		}
		cout << endl;

	}


	return 0;
}
