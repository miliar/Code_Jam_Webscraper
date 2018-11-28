#include <cstdio>
#include <algorithm>

using namespace std;

const int N = 1010;

int a[N];

int doit(int t) {
	int ans = 0;
	for (int i = N - 1; i > t; i--) {
		ans += ((i + t - 1) / t - 1) * a[i];
	}
	return ans + t;
}

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int tt = 0; tt < t; tt++) {
		fill(a, a + N, 0);
		int n;
		scanf("%d", &n); 
		for (int i = 0; i < n; i++) {
			int j;
			scanf("%d", &j);
			a[j]++;
		}
		int t1 = 1, t2 = 1000;
		while (true) {
			if (t2 - t1 < 3) {
				int ans = doit(t1);
				for (int i = t1 + 1; i <= t2; i++) {
					ans = min(ans, doit(i));
				}
				printf("Case #%d: %d\n", tt + 1, ans);
				break;
			}
			int j1 = t1 + (t2 - t1) / 3;
			int j2 =  j1 + (t2 - t1) / 3;
			if (doit(j1) >= doit(j2)) {
				t1 = j1;
			} else {
				t2 = j2;
			}
		}
	}		
}