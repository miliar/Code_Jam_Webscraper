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
const int N = 2e4 + 7;
const int INF = 2e9 + 7;
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
int ans, top;
char s[N], stk[N];
int main() {
	setIO("data");
	int T;
	scanf("%d", &T);
	rep(cas, 0, T) {
		scanf(" %s", s);
		ans = 0, top = 0;
		for (int i = 0; s[i]; ++i) {
			stk[++top] = s[i];
			if (top > 1 && stk[top - 1] == stk[top]) {
				ans += 10;
				top -= 2;
			}
		}
		ans += top / 2 * 5;
		printf("Case #%d: %d\n", cas + 1, ans);
	}
	return 0;
}
