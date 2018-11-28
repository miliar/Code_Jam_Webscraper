#include <bits/stdc++.h>
using namespace std;

#define MAXN 1005

int main() {
	int T; scanf("%d", &T);
	for(int ks = 0; ks < T; ks++) {
		printf("Case #%d: ", ks + 1);
		int N, a[MAXN];
		scanf("%d", &N);
		for(int i = 0; i < N; i++)
			scanf("%d", &a[i]);
		int ans = 0;
		for(int i = 1; i < N; i++)
			if(a[i - 1] > a[i])
				ans += a[i - 1] - a[i];
		printf("%d ", ans);
		int ma = 0;
		for(int i = 1; i < N; i++)
			ma = max(ma, a[i - 1] - a[i]);
		ans = 0;
		for(int i = 1; i < N; i++)
			ans += min(ma, a[i - 1]);
		printf("%d\n", ans);
	}
	return 0;
}
