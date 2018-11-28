#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <bitset>
#include <utility>
#include <numeric>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; ++i)
#define kep(i, n) for (int i = 1; i <=n; ++i)
#define fo(i, l, r) for (int i = l; i <= r; ++i)
#define fd(i, r, l) for (int i = r; i >= l; --i)
typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int, int> PII;
#define mp make_pair
#define pb push_back
#define N 222
#define c2(x) (1<<(x))

int T, n, kk;
double a[N], b[N], f[N][N];

double calc() {
    memset(f, 0, sizeof(f));
    f[0][0] = 1;
    kep(i, n) rep(j, min(i, kk/2) + 1) f[i][j] = f[i-1][j] * (1 - b[i]) + (j > 0 ? f[i-1][j-1] * b[i] : 0);
    return f[kk][kk/2];
}

void solve() {
	scanf("%d%d", &n, &kk);
	rep(i, n) scanf("%lf", &a[i]);
	sort(a, a + n);
	kep(i, kk/2) b[i] = a[i - 1];
	kep(i, kk/2) b[kk - i + 1] = a[n - i];
	double ans = calc();
    printf("%.9f\n", ans);
}

int main() {
    //freopen("b.in", "r", stdin);
	freopen("B-small-attempt0.in", "r", stdin);
	//freopen("B-small-attempt1.out", "w", stdout);
	scanf("%d", &T);
	kep(_, T) {
		printf("Case #%d: ", _);
		solve();
	}
}
