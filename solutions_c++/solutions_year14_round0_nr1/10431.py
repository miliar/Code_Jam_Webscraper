#include<iostream>

using namespace std;

const int N = 4;
int grid[N][N];
int answer1Array[N];
int grid2[N][N];
int answer2Array[N];

int main() {

	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	
	int caseCount;
	scanf("%d", &caseCount);
	for(int caseNumber = 1; caseNumber <= caseCount; caseNumber++){	
		int answer1;
		scanf("%d", &answer1);		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				scanf("%d", &grid[i][j]);
			}
		}
		
		for(int i = 0; i < N; i++) {
			answer1Array[i] = grid[answer1-1][i];
		}
		
		int answer2;
		scanf("%d", &answer2);
		for (int k = 0; k < N; k++) {
			for (int l = 0; l < N; l++) {
				scanf("%d", &grid2[k][l]);
			}
		}
		
		for(int k = 0; k < N; k++) {
			answer2Array[k] = grid2[answer2-1][k];
		}
		
		int count = 0;
		int target;
		for(int i = 0; i < N; i++ ) {
			for(int j = 0; j < N; j++ ) {
				if(answer1Array[i] == answer2Array[j]) {
					count++;
					target = answer1Array[i];
				}
			}
		}
		
		if(count == 1) {
			printf( "Case #%d: %d\n", caseNumber, target );
		} else if( count > 1 ) {
			printf( "Case #%d: Bad magician!\n", caseNumber );
		} else {
			printf( "Case #%d: Volunteer cheated!\n", caseNumber );
		}		
	}
	return 0;
}
