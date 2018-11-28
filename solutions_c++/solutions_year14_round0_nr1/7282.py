#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <unistd.h>
#include <algorithm>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <string>

#define pb push_back
#define mp make_pair
#define REP(i, N) for(int i = 0; i < (N); i++)

using namespace std;

int board[2][4][4];
int cnts[16];
int row[2];
int main() {
	int T, testcase=1;
	scanf("%d", &T);
	while(T--) {
		REP(i, 2) {
			scanf("%d", row+i);
			row[i]--;
			REP(j, 4) REP(k, 4) {
				scanf("%d", &board[i][j][k]);
				board[i][j][k]--;
			}
		}
		REP(i, 16) cnts[i] = 0;
		REP(i, 2) REP(k, 4) {
			cnts[board[i][row[i]][k]]++;								
		}
		bool cheated = true;
		bool badmag = false;
		int val = -1;
		
		REP(i, 16) if(cnts[i] > 1) {
			cheated = false;
			if(val != -1 && val != i)
				badmag = true;
			val = i;
		}

		printf("Case #%d: ", testcase++);
		if(cheated) printf("Volunteer cheated!");
		else if(badmag) printf("Bad magician!");
		else printf("%d", val+1);
		printf("\n");
	}
	
	return 0;
}
