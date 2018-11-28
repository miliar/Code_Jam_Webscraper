#include <cstdlib>
#include <cstdio>
#include <algorithm>

using namespace std;

const int N = 1000 + 10;

double a[N], b[N];
bool used[N];

bool cmp(int k, int n) {
	for(int i = 0; i < k; i++) {
		if(a[n - i - 1] < b[k - i - 1])	return false;
	}
	return true;
}

bool solve(double x, int n) {
	for(int i = 0; i < n; i++) {
		if(!used[i] && b[i] > x) {
			used[i] = true;
			return true;
		}
	}
	return false;
}

int main() {
	int t;
	scanf("%d", &t);

	for(int kase = 1; kase <= t; kase++) {
		int n;
		scanf("%d", &n);

		for(int i = 0; i < n; i++)	scanf("%lf", &a[i]);
		for(int i = 0; i < n; i++)	scanf("%lf", &b[i]);

		sort(a, a + n);
		sort(b, b + n);

		//for(int i = 0; i < n; i++)	printf("%d%c", (int) (a[i] * 1000), i == n - 1 ? '\n' : ' ');
		//for(int i = 0; i < n; i++)	printf("%d%c", (int) (b[i] * 1000), i == n - 1 ? '\n' : ' ');

		// solve y
		int y = 0;
		for(int i = n; i > 0; i--) {
			if(cmp(i, n)) {
				y = i;
				break;
			}
		}

		// solve z
		int z = 0;
		fill(used, used + n, false);
		for(int i = n - 1; i >= 0; i--) {
			if(!solve(a[i], n))	z++;
		}

		printf("Case #%d: %d %d\n", kase, y, z);
	}

	return 0;
}
