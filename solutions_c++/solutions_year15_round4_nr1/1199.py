#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <stack>
using namespace std;

#define RC_MAX 100
#define NONE '.'
#define UP '^'
#define DOWN 'v'
#define RIGHT '>'
#define LEFT '<'


int main(void) {
	int T;
	cin >> T;
	int R, C;
	char grid[RC_MAX][RC_MAX];
	char grid_temp[RC_MAX][RC_MAX];
	int ans;
	int i, j, k;
	for (int t=1; t<=T; t++) {
		cin >> R >> C;
		for (i=0; i<R; i++) {
			for (j=0; j<C; j++) cin >> grid[i][j];
		}
		/*
		for (i=0; i<R; i++) {
			for (j=0; j<C; j++) printf("%c", grid[i][j]);
			printf("\n");
		}
		printf("\n");
		*/
		ans = 0;
		for (int rotate=0; rotate<4; rotate++) {
		//	printf("rotate %d\n", rotate);
			
			//left edge
			for (i=0; i<R; i++) {
				j=0;
				int found=-1;
				while (j<C) {
					if (grid[i][j] == LEFT) { found = j; break; }
					else if (grid[i][j] == NONE) j++;
					else break;
				}
			//	printf("i %d, found %d\n", i, found);
				
				if (found != -1) {	//find new direction
					//try right
				//	printf("try right\n");
					for (j=found+1; j<C; j++) if (grid[i][j] != NONE) {
						grid[i][found] = RIGHT;
						ans++;
						goto left_done;
					}
					//try up
				//	printf("try up\n");
					for (k=i-1; k>=0; k--) if (grid[k][found] != NONE) {
						grid[i][found] = UP;
						ans++;
						goto left_done;
					}
					//try down
				//	printf("try down\n");
					for (k=i+1; k<R; k++) if (grid[k][found] != NONE) {
						grid[i][found] = DOWN;
						ans++;
						goto left_done;
					}
					ans = -1;
					goto finish;
				}
				left_done:;
			}
			
		//	printf("doing rotation\n");
			/*
			for (i=0; i<R; i++) {
				for (j=0; j<C; j++) printf("%c", grid[i][j]);
				printf("\n");
			}
			printf("\n");
			*/
			
			//rotate grid 90 clockwise
			for (i=0; i<R; i++) for (j=0; j<C; j++) {
				if (grid[i][j] == LEFT) grid_temp[i][j] = UP;
				else if (grid[i][j] == UP) grid_temp[i][j] = RIGHT;
				else if (grid[i][j] == RIGHT) grid_temp[i][j] = DOWN;
				else if (grid[i][j] == DOWN) grid_temp[i][j] = LEFT;
				else grid_temp[i][j] = NONE;
			}
			for (i=0; i<R; i++) for (j=0; j<C; j++) {
				grid[j][R-1-i] = grid_temp[i][j];
			}
			swap(R, C);
			
			/*
			for (i=0; i<R; i++) {
				for (j=0; j<C; j++) printf("%c", grid[i][j]);
				printf("\n");
			}
			printf("\n");
			*/
		}
		
		finish:;
		
		printf("Case #%d: ", t);
		if (ans == -1) printf("IMPOSSIBLE");
		else printf("%d", ans);
		printf("\n");
	}
	return 0;
}