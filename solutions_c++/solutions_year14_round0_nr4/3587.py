#include <cstdio>
#include <set>
#include <algorithm>
#include <cmath>

using namespace std;

int naomi[1010], ken[1010];
int p[1010];

void show(int a[], int n) {
	for (int i = 0; i < n; i++)
		printf("%d%c", a[i], i == n - 1 ? '\n' : ' ');
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int qwe;
	scanf("%d", &qwe);
	for (int t = 1; t <= qwe; t++) {
		int n;
		scanf("%d", &n);
		double x;
		for (int i = 0; i < n; i++) {
			scanf("%lf", &x);
			naomi[i] = floor(x * 1e5 + 1e-9);
		}
		sort(naomi, naomi + n);
		// show(naomi, n);
		for (int i = 0; i < n; i++) {
			scanf("%lf", &x);
			ken[i] = floor(x * 1e5 + 1e-9);
		}
		sort(ken, ken + n);
		// show(ken, n);
		for (int i = 0; i < n; i++)
			p[i] = i;
		int war = 0;
		set<int> s;
		for (int i = 0; i < n; i++)
			s.insert(ken[i]);
		for (int i = n - 1; i >= 0; i--)
			if (naomi[i] > *s.rbegin()) {
				war++;
				s.erase(s.begin());
			}
			else
				s.erase(s.upper_bound(naomi[i]));
		int dwar = 0;
		for (int i = 0, ki = 0; i < n; i++)
			if (naomi[i] > ken[ki]) {
				dwar++;
				ki++;
			}
		printf("Case #%d: %d %d\n", t, dwar, war);
	}
	return 0;
}
