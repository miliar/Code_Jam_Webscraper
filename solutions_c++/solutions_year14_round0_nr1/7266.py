#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <map>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)
#define kep(i, n) for (int i = 1; i <=n; i++)

int T, a[4][4], k;

void solve() {
	scanf("%d", &k); k--;
	rep(i, 4) rep(j, 4) scanf("%d", &a[i][j]);
	map<int, int> ss;
	rep(j, 4) ss[a[k][j]]++;
	scanf("%d", &k); k--;
	rep(i, 4) rep(j, 4) scanf("%d", &a[i][j]);
	rep(j, 4) ss[a[k][j]]++;
	int ans, num = 0;
	for (map<int, int>::iterator p = ss.begin(); p != ss.end(); p++) {
		if (p->second == 2) {
			num++; ans = p->first;
		}
	}
	if (num == 0) puts("Volunteer cheated!"); else
	if (num > 1) puts("Bad magician!"); else
	printf("%d\n", ans);
}

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.ou", "w", stdout);
	scanf("%d", &T);
	kep(_, T) {
		printf("Case #%d: ", _);
		solve();
	}
}
