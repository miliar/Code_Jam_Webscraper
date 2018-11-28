#include <stdio.h>
#include <algorithm>

using namespace std;

int mat[128][128], mil[128], mic[128];

int main()
{
	int T;
	scanf("%d", &T);
	for(int ca = 1; ca <= T; ca++) {
		int n, m, ok = 1;
		scanf("%d%d", &n, &m);

		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
				scanf("%d", &mat[i][j]);

		for(int i = 0; i < n; i++) {
			mil[i] = mat[i][0];
			for(int j = 0; j < m; j++)
				mil[i] = max(mil[i], mat[i][j]);
		}

		for(int i = 0; i < m; i++) {
			mic[i] = mat[0][i];
			for(int j = 0; j < n; j++)
				mic[i] = max(mic[i], mat[j][i]);
		}

		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
				if(mat[i][j] != min(mil[i],mic[j]))
					ok = 0;
		printf("Case #%d: %s\n", ca, ok ? "YES" : "NO");
	}
	return 0;
}
