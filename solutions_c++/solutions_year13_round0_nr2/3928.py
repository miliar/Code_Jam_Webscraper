#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <string>
#include <map>

using namespace std;

int grid[200][220];
int n, m;

int main() {
	
	int casos, caso = 0;
	scanf("%d", &casos);
	
	while(casos--){ 
		caso++;
		
		printf("Case #%d: ", caso);
		
		scanf("%d%d", &n, &m);
		
		for(int i = 0; i < n; ++i) {
			for(int j = 0; j < m; ++j) {
				scanf("%d", &grid[i][j]);
			}
		}
		
		for( int i = 0; i < n; ++i ) {
			for(int j = 0; j < m; ++j) {
				int at = grid[i][j];
				bool ok1 = true, ok2 = true;
				//printf(">> %d %d\n", i, j);
				for (int a = 0; a < n; ++a) {
					//printf("%d %d\n", a, j);
					if (grid[a][j] > at) {
						ok1 = false; break;
					}
				}
				for (int a = 0; a < m; ++a) {
					//printf("%d %d\n", i, a);
					if (grid[i][a] > at) {
						ok2 = false; break;
					}
				}
				if (!ok1 && !ok2) {
					printf("NO\n");
					goto cont;
				}
			}
		}
		printf("YES\n");
		cont:;
		
	}
	
	return 0;
}