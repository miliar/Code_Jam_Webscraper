#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)
#define kep(i, n) for (int i = 1; i <=n; i++)

double zz = 1e-7;
int T;
double c, f, x, s, ans;

bool zero(double x) {
    return abs(x) < zz;
}

bool better(double x, double y) {
    return (x < y || zero(x-y));
}

void solve() {
	scanf("%lf%lf%lf", &c, &f, &x);
	s = 2; ans = 0;
	while (better(x/(s+f)+c/s, x/s)) {
		ans += c/s; s += f;
	}
	ans += x/s;
	printf("%.7lf\n", ans);
}

int main() {
    freopen("b.in", "r", stdin);
    freopen("b.ou", "w", stdout);
	scanf("%d", &T);
	kep(_, T) {
		printf("Case #%d: ", _);
		solve();
	}
}
