#include <stdio.h>
#include <algorithm>
int d[10005];
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("ans1_l.txt", "w", stdout);
	int task_no, i, N, T, X, st, en, ans;
	scanf("%d", &T);
	for(task_no = 1; task_no <= T; task_no++) {
		scanf("%d %d", &N, &X);
		for(i = 1; i <= N; i++) scanf("%d", &d[i]);
		std::sort(d+1, d+N+1);
		st = 1, en = N;
		ans = 0;
		while(st <= en) {
			if(d[st]+d[en] <= X) st++;
			en--;
			ans++;
		}
		printf("Case #%d: %d\n", task_no, ans);
	}
	return 0;
}