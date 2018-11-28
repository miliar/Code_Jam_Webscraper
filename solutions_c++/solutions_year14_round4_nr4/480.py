#include <cstdio>
#include <cstring>

using namespace std;

const int MAXN = 11;

int cm[MAXN][MAXN];
int id[MAXN], f[MAXN];
char st[MAXN][MAXN];
int n, m, ans1, ans2;

void check()
{
	int cur = 0;
	for (int i = 0; i < m; i ++)
		if (f[i] > 0) cur ++;
	for (int i = 0; i < n; i ++){
		int l = 0;
		for (int j = 0; j < i; j ++)
			if (id[j] == id[i] && cm[i][j] > l)
				l = cm[i][j];
		cur += strlen(st[i]) - l;
	}
	if (cur > ans1)
		ans1 = cur, ans2 = 1;
	else if (cur == ans1)
		ans2 ++;
}

void dfs(int t)
{
	if (t == n){
		check(); return;
	}
	if (t == 0){
		id[t] = 0; f[0] = 1;
		dfs(t + 1);
		//f[0] = 0;
	} else {
		for (int i = 0; i < m; i ++){
			id[t] = i; f[i] ++;
			dfs(t + 1);
			f[i] --;
		}
	}
}

int main()
{
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t ++){
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i ++)
			scanf("%s", st[i]);
		memset(f, 0, sizeof(f));
		for (int i = 0; i < n; i ++)
			for (int j = 0; j < n; j ++){
				cm[i][j] = 0;
				int l = strlen(st[i]);
				int l2 = strlen(st[j]);
				if (l2 < l) l = l2;
				int k = 0;
				while (k < l && st[i][k] == st[j][k])
					cm[i][j] ++, k ++;
			}
		ans1 = -1;
		dfs(0);
		printf("Case #%d: %d %d\n", t + 1, ans1, ans2 * m);
	}
	return 0;
}
