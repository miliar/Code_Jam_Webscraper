#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

#define N 20
#define INF 2000000000
#define eps 1e-6

int n, k;
double ans;
double a[N];
int use[N];
double temp_ans;

void update(int total, int num, double sum) {
	if (total == k) {
		if (num == 0)
			temp_ans += sum;
		return;
	}
	if (num > 0) {
		double temp = sum * a[use[total]];
		update(total + 1, num - 1, temp);
	}
	double temp = sum * (1 - a[use[total]]);
	update(total + 1, num, temp);
}

void solve(int total, int num) {
	if (total == n) {
		if (num == 0) {
			temp_ans = 0;
			update(0, k / 2, 1.0);
			ans = max(ans, temp_ans);
		}
		return;
	}
	if (num > 0) {
		use[k - num] = total + 1;
		solve(total + 1, num - 1);
	}
	solve(total + 1, num);
}

int main() {
	int ncas;
	scanf("%d", &ncas);
	for (int tcas = 1; tcas <= ncas; tcas++) {
		scanf("%d%d", &n, &k);
		for (int i = 1; i <= n; i++) {
			scanf("%lf", &a[i]);
		}
		ans = -INF;
		solve(0, k);
		printf("Case #%d: %lf\n", tcas, ans);
	}
	return 0;
}