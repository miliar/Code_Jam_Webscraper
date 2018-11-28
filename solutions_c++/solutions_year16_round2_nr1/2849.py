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

	string table[10] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
	rep(_, T) {
		cout << "Case #" << _ + 1 << ": ";
		string s;
		cin >> s;
		map<char, int> mp;
		rep(i, s.size()) {
			mp[s[i]]++;
		}
		string ans;
		rep(i, 10) {
			rep(j, table[i].size()) {

				bool ok = true;
				rep(k, 10) if(i != k){
					rep(l, table[k].size()) {
						if (table[i][j] == table[k][l]) {
							ok = false;
						}
					}
				}

				if (ok) {
					int count = 0;
					rep(k, table[i].size()) {
						if (table[i][j] == table[i][k]) {
							count++;
						}
					}
					count = mp[table[i][j]] / count;
					rep(k, count) {
						rep(l, table[i].size()) {
							mp[table[i][l]]--;
						}
						ans += tostr(i);
					}
				}
			}
		}

		set<map<int, int>> vis;
		bool end = false;
		function<void(map<int,int>)> solve = [&](map<int, int> &use) {
			if (end)return;
			if (vis.count(use))return;
			vis.insert(use);
			bool ok = true;
			each(i, use) {
				rep(j, table[i.first].size()) {
					mp[table[i.first][j]] -= i.second;
					if (mp[table[i.first][j]] < 0)ok = false;
				}
			}
			end = true;
			each(i, mp) {
				if (i.second != 0)end = false;
			}
			if (end) {
				each(i, use) {
					rep(j, i.second) {
						ans += tostr(i.first);
					}
				}
				sort(all(ans));
				return;
			}
			each(i, use) {
				rep(j, table[i.first].size()) {
					mp[table[i.first][j]] += i.second;
				}
			}
			if (ok) {
				for (int i = 0; i <= 9; i++) {
					use[i]++;
					solve(use);
					use[i]--;
				}
			}
			return;
		};
		solve(map<int,int>());
		cout << ans << endl;
	}

	return 0;
}
