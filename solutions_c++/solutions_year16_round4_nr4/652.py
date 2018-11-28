#include <stdio.h>
#include <memory.h>

#define N 10
#define INF 1000000000

int n;
int ad[N][N];
int ans;

int pc[N], mc[N];

bool go_check(int lev)
{
	if (lev > n) return true;

	for (int i = 1; i <= n; i++) {
		if (pc[i]) continue;
		pc[i] = true;

		bool flag = false;
		for (int j = 1; j <= n; j++) {
			if (ad[i][j] && !mc[j]) {
				flag = true;
				mc[j] = true;
				if (!go_check(lev + 1)) return false;
				mc[j] = false;
			}
		}
		if (!flag) return false;
		pc[i] = false;
	}

	return true;
}

void func(int i, int j, int cost)
{
	if (i > n) {
		memset(pc, 0, sizeof(pc));
		memset(mc, 0, sizeof(mc));
		if(go_check(1) && cost < ans) ans = cost;
		return;
	}
	else if (j > n) func(i + 1, 1, cost);
	else {
		func(i, j + 1, cost);
		if (!ad[i][j]) {
			ad[i][j] = 1;
			func(i, j + 1, cost + 1);
			ad[i][j] = 0;
		}
	}
}

void process()
{
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) scanf("%1d", &ad[i][j]);
	}
	ans = INF;

	func(1, 1, 0);

	printf("%d\n", ans);
}

int main()
{
	freopen("D-small-attempt1.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		process();
	}
	return 0;
}