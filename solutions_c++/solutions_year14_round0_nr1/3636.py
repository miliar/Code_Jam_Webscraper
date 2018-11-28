#include <bits/stdc++.h>
using namespace std;

#define fileName "A-small-attempt0"
int caseNum = 0;

int grid[4][4];
int rSet[4];

void readGrid() {
	for(int i = 0; i < 4; i++) {
		for(int j = 0; j < 4; j++){
			scanf(" %d", &grid[i][j]);
		}
	}
}

void solve() {
    printf("Case #%d: ", ++caseNum);
	
	int rAns, cAns;
	scanf(" %d", &rAns);
	rAns--;
	
	readGrid();
		
	for(int i = 0; i < 4; i++) {
		rSet[i] = grid[rAns][i];
	}
	
	scanf(" %d", &rAns);
	rAns--;
	
	readGrid();
	
	bool found = false;
	
	for(int i = 0; i < 4; i++) {
		for(int j = 0; j < 4; j++) {
			if(rSet[i] == grid[rAns][j] && !found) {
				found = true;
				cAns = j;
				break;
			}
			if(found && rSet[i] == grid[rAns][j]) {
				printf("Bad magician!\n");
				return;
			}
		}
	}
	
	if(found)
		printf("%d\n", grid[rAns][cAns]);
	else
		printf("Volunteer cheated!\n");
}

int main() {
    freopen(fileName ".in", "r", stdin);
    freopen(fileName ".txt", "w", stdout);
    
    int T;
    scanf("%d", &T);
	while(T--) {
        solve();
    }
    return 0;
}