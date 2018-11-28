#include <stdio.h>

int n, m;
int lawn[110][110];
bool lin(int a, int b)
{
for(int i = 0; i < m; i++)
	if(lawn[a][i] > b)
		return true;
return false;
}

bool col(int a, int b)
{
for(int i = 0; i < n; i++)
	if(lawn[i][a] > b)
		return true;
return false;
}

int
main(void)
{
int i, j, T, test, k;
scanf("%d", &T);
for(test = 1; test <= T; test++)
	{
	bool answer = true;
	scanf("%d %d", &n, &m);
	for(i = 0; i < n; i++)
		for(j = 0; j < m; j++)
			scanf("%d", &lawn[i][j]);
	for(i = 0; i < n && answer; i++)
		for(j = 0; j < m && answer; j++)
			if((col(j, lawn[i][j]) && lin(i, lawn[i][j])))
				answer = false;
	printf("Case #%d: %s\n", test, answer ? "YES" : "NO");
	}
return 0;
}
