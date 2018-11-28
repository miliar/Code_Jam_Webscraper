#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
using namespace std;
const int n_MAX = 1005; 
int T;
int main() {
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int n, ans1(0), ans2(0);
		double a[n_MAX], b[n_MAX];
		bool fa[n_MAX], fb[n_MAX];
		memset(fa, 1, sizeof(fa));
		memset(fb, 1, sizeof(fb));
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) scanf("%lf", a + i);
		for (int i = 0; i < n; ++i) scanf("%lf", b + i);
		sort(a, a + n);
		sort(b, b + n);
		for (int i = 0; i < n; ++i) 
			for (int j = 0; j < n; ++j) 
				if (b[j] > a[i] && fb[j]){fb[j] = 0; ++ans2; break;}
		for (int i = 0; i < n; ++i) 
			for (int j = 0; j < n; ++j)
				if (a[j] > b[i] && fa[j]){fa[j] = 0; ++ans1; break;}
			
		printf("Case #%d: %d %d\n",t, ans1, n - ans2);
	}
	return 0;
}

