#include <iostream>
#include <cstdio>
#include <string>
#include <ctime>

using namespace std;
typedef long long ll;
#define err(...) fprintf(stderr,__VA_ARGS__)

const int MAX = 100;
int R,C;
char grid[MAX][MAX];

void doCase(int t) {
	cin >> R >> C;
	for (int r=0; r<R; r++) {
		string l; cin >> l;
		for (int c=0; c<C; c++) {
			grid[r][c] = l[c];
		}
	}
	
	printf("Case #%d: ",t);
	int res = 0;
	for (int r=0; r<R; r++) {
		for (int c=0; c<C; c++) {
			if (grid[r][c] == '.') continue;
			bool up,down,left,right;
			up = down = left = right = false;
			for (int l=1; l<max(R,C); l++) {
				if (r-l >= 0 && grid[r-l][c] != '.') up = true;
				if (r+l < R && grid[r+l][c] != '.') down = true;
				if (c-l >= 0 && grid[r][c-l] != '.') left = true;
				if (c+l < C && grid[r][c+l] != '.') right = true;
			}

			if ( (grid[r][c] == '^' && !up) || (grid[r][c] == 'v' && !down) || (grid[r][c] == '<' && !left) || (grid[r][c] == '>' && !right) ) {
				//Arrow must be moved
				if (!(up || down || left || right)) { //No way to aim it
					printf("IMPOSSIBLE\n");
					return;
				} else {
					res++;
				}
			}
		}
	}
	printf("%d\n",res);
}

// PROBLEM NON-SPECIFIC TEMPLATE CODE FOLLOWS

int main() {
	int T; cin >> T;
	err("There are %d cases.\n",T);
	
	clock_t prev,cur = clock();
	clock_t start = cur;
	for (int t=1; t<=T; t++) {
		doCase(t);
		prev = cur;
		cur = clock();
		err("_%d(%d)_",t, (int) ( 1000*(cur - prev) / ((int)CLOCKS_PER_SEC) ));
	}
	err("\nFinished %d cases in %d milliseconds.\n",T,(int) ( 1000*(cur-start) / ((int)CLOCKS_PER_SEC) ));
}
