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
int n, s;
bool vis[N];
struct Node {
	int x, y, z, dx, dy, dz;
	void in() {
		scanf("%d%d%d%d%d%d", &x, &y, &z, &dx, &dy, &dz);
	}
} a[N];
int dis2(const Node &p, const Node &q) {
	return sqr(p.x - q.x) + sqr(p.y - q.y) + sqr(p.z - q.z);
}
queue<int> que;
bool check(int mx) {
	rep(i, 0, n)
		vis[i] = false;
	vis[0] = true, que.push(0);
	while (!que.empty()) {
		int u = que.front();
		que.pop();
		rep(i, 0, n) {
			if (vis[i])
				continue;
			if (dis2(a[u], a[i]) <= mx) {
				vis[i] = true;
				que.push(i);
			}
		}
	}
	return vis[1];
}
int main() {
//	debug("data");
	setIO("data");
	int T;
	scanf("%d", &T);
	rep(cas, 0, T){
		scanf("%d%d", &n, &s);
		rep(i, 0, n)
			a[i].in();
		int l = 0, r = INF;
		while (l + 1 < r) {
			int mid = (l + r) >> 1;
			check(mid) ? r = mid : l = mid;
		}
		int ans = check(l) ? l : r;
		printf("Case #%d: %.10lf\n", cas + 1, sqrt(1. * ans));
	}
	return 0;
}
