#include <cstdio>
int answer, n;
bool s[1010][1010];
bool visit[1010];
int ans[1010];
void backtrack(int cur, int count) {
	int i;
	bool flag = true;
	visit[cur] = true;
	for(i=0;i<count;++i) {
		if(s[ans[i]][ans[(i+1)%count]] || s[ans[i]][ans[(i-1+count)%count]])
			continue;
		flag = false;
	}
	if(flag) {
		if(count > answer)
			answer = count;
	}
	for(i = 1;i<=n;++i) {
		if(visit[i])
			continue;
		ans[count] = i;
		backtrack(i, count+1);
		visit[i] = false;
	}
}
int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	int t, i, j, a;
	scanf("%d", &t);
	for(int x = 1;x<=t;++x) {
		scanf("%d", &n);
		for(i = 1;i<=n;++i) {
			visit[i] = false;
			for(j=1;j<=n;++j)
				s[i][j] = 0;
		}
		for(i = 1;i<=n;++i) {
			scanf("%d", &a);
			s[i][a] = 1;
		}
		printf("Case #%d: ", x);
		answer = 0;
		for(i=1;i<=n;++i) {
			ans[0] = i;
			backtrack(i, 1);
			visit[i] = false;
		}
		printf("%d\n", answer);
	}
	return 0;
}
