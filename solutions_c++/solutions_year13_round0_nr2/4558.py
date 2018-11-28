#include <cstdio>
#include <cstdlib>

using namespace std;

int grid[200][200];

bool solve() {
	int m,n;
	scanf("%d %d",&m,&n);
	
	for (int i=0; i<m; ++i) {
		for (int j=0; j<n; ++j) {
			scanf("%d",&grid[i][j]);
		}
	}
	
	int numrows = m;
	int numcolumns = n;
	
	while ( numrows > 0 && numcolumns > 0 ) {
		int minimum = 200;
		int ii,jj; // coordinate del minimo
		
		for (int i=0; i<m; ++i) {
			for (int j=0; j<n; ++j) {
				if ( grid[i][j] > 100 ) continue;
				if ( grid[i][j] < minimum ) {
					minimum = grid[i][j];
					ii = i;
					jj = j;
				}
			}
		}
		//printf("Minimo: %d\n",minimum);
		
		bool tryrow = 1;
		for (int j=0; j<n; ++j) {
			if ( grid[ii][j] != minimum && grid[ii][j] <= 100 ) {
				tryrow = 0;
				break;
			}
		}
		
		if ( tryrow ) {
			for (int j=0; j<n; ++j) {
				grid[ii][j] = 200;
			}
			numrows--;
			//printf("Tolgo la riga %d\n",ii);
		}
		
		bool trycol = 1;
		for (int i=0; i<m; ++i) {
			if ( grid[i][jj] != minimum && grid[i][jj] <= 100 ) {
				trycol = 0;
				break;
			}
		}
		
		if ( trycol ) {
			for (int i=0; i<m; ++i) {
				grid[i][jj] = 200;
			}
			numcolumns--;
			//printf("Tolgo la colonna %d\n",jj);
		}
		
		if ( !tryrow && !trycol ) return 0;
	}
	
	return 1;
}

int main() {
	
	int t;
	scanf("%d",&t);
	
	for (int i=1; i<=t; ++i) {
		bool res = solve();
		printf("Case #%d: ",i);
		if ( res ) printf("YES\n");
		else printf("NO\n");
	}
	
	return 0;
}
