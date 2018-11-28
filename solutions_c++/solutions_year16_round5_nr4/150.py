#include<time.h>
#include<stdlib.h>
#include<assert.h>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<set>
#include<map>
#include<queue>
#include<bitset>
#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;
typedef long long ll;
typedef unsigned long long ul;
typedef vector<int> vi;
typedef pair<int, int> pii;
#define rep(i,l,r) for(int i=l;i<(r);++i)
#define per(i,l,r) for(int i=r-1;i>=(l);--i)
#define sz(x) ((int)((x).size()))
#define sqr(x) ((x)*(x))
#define all(x) (x).begin(),(x).end()
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define de(x) cout << #x << " = " << x << endl;
#define debug(x) freopen(x".in", "r", stdin);
#define setIO(x) freopen(x".in", "r", stdin);freopen(x".out", "w", stdout);
const ll LINF = 1e17 + 7;
const ul BASE = 33;
const int N = 1e3 + 7;
const int INF = 1e9 + 7;
const int MOD = 1e9 + 7;
const double Pi = acos(-1.);
const double EPS = 1e-8;
ll kpow(ll a, ll b) {
	ll ret = 1;
	for (; b; b >>= 1, a = a * a)
		if (b & 1)
			ret = ret * a;
	return ret;
}
//--------------head--------------
int n, m;
string B;
vector<string> G;
int main() {
//	debug("data");
	setIO("data");
	int T;
	cin >> T;
	rep(cas, 0, T){
		cin >> n >> m;
		G.clear();
		rep(i, 0, n) {
			string str;
			cin >> str;
			G.pb(str);
		}
		cin >> B;
		bool flag = false;
		rep(i, 0, n)
			if (B == G[i]) {
				flag = true;
				break;
			}
		printf("Case #%d: ", cas + 1);
		if (flag) {
			cout << "IMPOSSIBLE";
		} else {
			string l = "", r = "";
			rep(i, 0, m)
				l.append("0?");
			rep(i, 1, m)
				r.append("1");
			r.append("0");
			cout << l << " " << r;
		}
		cout << endl;
//		printf("Case #%d: %.10lf\n", cas + 1, sqrt(1. * ans));
	}
	return 0;
}
