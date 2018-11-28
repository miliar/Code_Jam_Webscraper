#include <cstdio>

using namespace std;

void solve(int t)
{
	printf("Case #%d: ", t);
	int a[100][100], n, m, row[100] = {}, col[100] = {};
	scanf("%d%d", &n, &m);
	for(int i = 0; i < n; ++i)
		for(int j = 0; j < m; ++j)
			scanf("%d", &a[i][j]);
	for(int i = 0; i < n; ++i)
		for(int j = 0; j < m; ++j)
		{
			if(row[i] == 0 || a[i][j] > row[i])
				row[i] = a[i][j];
			if(col[j] == 0 || a[i][j] > col[j])
				col[j] = a[i][j];
		}
	for(int i = 0; i < n; ++i)
		for(int j = 0; j < m; ++j)
			if(a[i][j] < row[i] && a[i][j] < col[j])
			{
				printf("NO\n");
				return;
			}
	printf("YES\n");
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int k = 1; k <= t; ++k)
		solve(k);
	return 0;
}