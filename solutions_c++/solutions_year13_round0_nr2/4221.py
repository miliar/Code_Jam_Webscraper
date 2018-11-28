#include <cstdio>

#define MAXSIZE 101
#define FOR(a,b,c) for(a=b;a<c;a++)

using namespace std;

int mat [MAXSIZE][MAXSIZE];
int maxr [MAXSIZE];
int maxc [MAXSIZE];

int main () {

	int TC, cc, r, c;
	int rl, cl;
	bool res;
	
	scanf("%d", &TC);
	FOR (cc,0,TC) {
		
		// reset data
		FOR (c, 0, MAXSIZE) {
			maxc[c] = 0;
		}
		FOR (r, 0, MAXSIZE) {
			maxr[r] = 0;
		}
		
		//get input
		scanf("%d %d", &rl, &cl);
		FOR (r, 0, rl) {
			FOR (c, 0, cl) {
				scanf("%d", &(mat[r][c]));
			}
		}
		
		// get the max for each row and col
		FOR (r, 0, rl) {
			FOR (c, 0, cl) {
				if ( mat[r][c] > maxc[c] ) {
					maxc[c] = mat[r][c];
				}
				if ( mat[r][c] > maxr[r] ) {
					maxr[r] = mat[r][c];
				}
			}
		}
		
		// check if possible
		res = true;
		FOR (r, 0, rl) {
			FOR (c, 0, cl) {
				if ( mat[r][c] < maxr[r] && mat[r][c] < maxc[c] ) {
					res = false;
					break;
				}
			}
			if ( res == false ) break;
		}
		
		if ( res )
			printf("Case #%d: YES\n", cc+1);
		else
			printf("Case #%d: NO\n", cc+1);
				
		
		/*/ test output
		FOR (r, 0, rl) {
			FOR (c, 0, cl) {
				printf("%2d", mat[r][c]);
			}
			printf("\n");
		}
		FOR (c, 0, cl) {
			printf("%2d ", maxc[c]);
		}
		printf("\n");
		FOR (r, 0, rl) {
			printf("%2d\n", maxr[r]);
		}*/
		
	}

	return 0;
}
