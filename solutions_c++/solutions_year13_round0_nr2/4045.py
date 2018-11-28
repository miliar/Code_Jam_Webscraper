//Jakub "Cubix651" Cisło
//Task: Lawnmower
#include <cstdio>

const int MAX = 102;
int lawn[MAX][MAX], n, m;

bool checkPart(int x, int y)
{
	bool g = false, h = false;
	
	for(int i = 0; i < n; ++i)
		if(lawn[i][y] > lawn[x][y])
			g = true;
	
	for(int i = 0; i < m; ++i)
		if(lawn[x][i] > lawn[x][y])
			h = true;
	return (g && h);
}

bool solve()
{
	scanf("%d%d", &n, &m);
	for(int i = 0; i < n; ++i)
		for(int j = 0; j < m; ++j)
			scanf("%d", &lawn[i][j]);
	
	for(int i = 0; i < n; ++i)
		for(int j = 0; j < m; ++j)
			if(checkPart(i, j))
				return false;
	return true;
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; ++t)
		printf("Case #%d: %s\n", t, solve()?"YES":"NO");
	return 0;
}
