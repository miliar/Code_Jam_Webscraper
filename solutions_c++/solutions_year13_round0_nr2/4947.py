#include <cstdio>
#include <cstdlib>

using namespace std;

#define MAXN 105
#define MAXM 105

int field[MAXN][MAXM];

int main()
{
//	freopen("B-large.in", "r", stdin);
//	freopen("B_large.txt", "w", stdout);
	
	int T;
	scanf("%d", &T);
	
	for (int t = 1; t <= T; t++)
	{
		int n, m;
		scanf("%d %d", &n, &m);
		
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				scanf("%d", &field[i][j]);
		
		bool flag = true;
		
		for (int i = 0; i < n and flag; i++)
			for (int j = 0; j < m and flag; j++) {
				bool ok = true;
				for (int k = 0; k < n; k++) if (field[k][j] > field[i][j]) ok = false;
				if (ok) continue;
				
				ok = true;
				for (int k = 0; k < m; k++) if (field[i][k] > field[i][j]) ok = false;
				if (!ok) flag = false;
			}
		
		printf("Case #%d: ", t);
		printf("%s\n", flag ? "YES" : "NO");
	}
	
//	fclose(stdin);
//	fclose(stdout);
	
	return 0;
}
