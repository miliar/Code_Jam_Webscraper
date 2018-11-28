#include <cstdio>
#include <cstdlib>
#include <cmath>
#define MAXLEN 120
#define MAXN 120


using namespace std;

int tc, cc, n;
char buf [MAXLEN];
int grid [MAXN][MAXLEN];
int dif [MAXN];
char let [MAXN][MAXLEN];

int main () {
	
	scanf("%d", &tc);
	for ( cc = 1; cc <= tc; ++cc ) {
	
		scanf("%d", &n);
		for ( int i = 0; i < n; ++i ) {
			scanf("%s", buf);
			
			char last = buf[0];
			int count = 1;
			int idx = 0; 
			for ( int x = 1; buf[x-1] != 0; ++x ) {
				if ( buf[x] != last ) {
					grid[i][idx] = count;
					let[i][idx] = last;
					last = buf[x];
					count = 0;
					idx += 1;
				}
				count += 1;
			}
			
			dif[i] = idx;
		}
		
		bool invalid = false;
		for ( int i = 1; i < n; ++i ) {
			if ( dif[i] != dif[i-1] ) {
				invalid = true;
				break;
			}
		}
		for ( int i = 1; i < n; ++i ) {
			for ( int c = 0; c < dif[i]; ++c ) {
				if ( let[i][c] != let[i-1][c] ) {
					invalid = true;
					break;
				}
			}
		}
		if ( invalid ) {
			printf("Case #%d: Fegla Won\n", cc);
			continue;
		}
		
		int sum = 0;
		int sub;
		int med;
		int col;
		for ( col = 0; col < dif[0]; ++col ) {
			sub = 0; 
			for ( int l = 0; l < n; ++l ) {
				sub += grid[l][col];
			}
			med = round( sub / float(n) );
			
			//printf("MED sub=%d, col=%d is med=%d\n", sub, col, med);
			
			for ( int l = 0; l < n; ++l ) {
				sum += abs( grid[l][col] - med );
			}
		}
		
		
		
		/*/DEBUG
		for ( int i = 0; i < n; ++i ) {
			printf("GRID[%d]:", i);
			for ( int k = 0; k < dif[i]; ++k ) {
				printf(" %d", grid[i][k]);
			}
			printf(" - len=%d\n", dif[i]);
		}*/
		
		
		
		printf("Case #%d: %d\n", cc, sum);
	}
	
	return 0;
}


				
