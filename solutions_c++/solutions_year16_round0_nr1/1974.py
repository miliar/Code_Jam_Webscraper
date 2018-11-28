#include<stdlib.h>
#include<time.h>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<set>
#include<queue>
#include<bitset>
#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;
typedef long long LL;
typedef unsigned long long UL;
typedef vector<int> vi;
typedef pair<int, int> pii;
#define sz(x) ((int)(x.size()))
#define sqr(x) ((x)*(x))
#define pb push_back
#define mp make_pair
#define fi first
#define se second
const int N = 1e2 + 7;
const int M = 1e6 + 7;
const int INF = 2e5 + 7;
const int MOD = 1e9 + 7;
const LL LINF = 1e17 + 7;
const double Pi = acos(-1.);
const double EPS = 1e-8;
bool f[10];
LL solve(int n) {
	if (n == 0)
		return -1;
	memset(f, false, sizeof(f));
	int cnt = 0;
	LL x = 0, y;
	while (cnt < 10) {
		x += n;
		y = x;
		while (y > 0) {
			if (!f[y % 10]) {
				++cnt;
				f[y % 10] = true;
			}
			y /= 10;
		}
	}
	return x;
}
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T, tt = 0;
	scanf("%d", &T);
	while (T--) {
		int n;
		scanf("%d", &n);
		printf("Case #%d: ", ++tt);
		LL ret = solve(n);
		if (ret == -1) {
			puts("INSOMNIA");
		} else {
			printf("%I64d\n", ret);
		}
	}
	return 0;
}
