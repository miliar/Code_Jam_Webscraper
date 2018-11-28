#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int n,m;
int orig[200][200];
int grid[200][200];

int main(){
	int exec = 0;
	int t; scanf("%d", &t); while (t--){
		scanf("%d %d", &n, &m);
		for (int i = 0; i<n; i++)
			for (int j = 0; j<m; j++)
				scanf("%d", &orig[i][j]), grid[i][j] = 100;

		for (int i = 0; i<n; i++){
			int maxx = 0;
			for (int j = 0; j<m; j++)
				maxx = max(maxx, orig[i][j]);
			for (int j = 0; j<m; j++)
				grid[i][j] = min(grid[i][j], maxx);
		}

		for (int j = 0; j<m; j++){
			int maxx = 0;
			for (int i = 0; i<n; i++)
				maxx = max(maxx, orig[i][j]);
			for (int i = 0; i<n; i++)
				grid[i][j] = min(grid[i][j], maxx);
		}

		char ok = 1;
		for (int i = 0; i<n; i++){
			for (int j = 0; j<m; j++){
				if (grid[i][j] != orig[i][j]){
					ok = 0; break;
				}
			} 
			if (!ok) break;
		}

		printf("Case #%d: %s\n", ++exec, ok?"YES":"NO");
	}
	return 0;
}