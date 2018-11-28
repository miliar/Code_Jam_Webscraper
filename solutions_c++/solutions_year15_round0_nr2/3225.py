#include <bits/stdc++.h>
using namespace std;
int n, T, a[1111];
int main(){	
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);

	scanf("%d", &T);
	for (int test = 1; test <= T; test++){
		scanf("%d", &n);
		for (int i = 1; i <= n; i++) scanf("%d", a + i);

		int ans = 1000;
		for (int eat_time = 1; eat_time <= 1000; eat_time++){
			int devide_time = 0;
			for (int i = 1; i <= n; i++){
				devide_time += (a[i] / eat_time) - ((a[i] % eat_time) == 0);
			}
			ans = min(ans, eat_time + devide_time);
		}
		printf("Case #%d: %d\n", test, ans);
	}
	return 0;
}