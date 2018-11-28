#include <stdio.h>

using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++){
		int N = 4;
		int row1, row2;
		int prvi[4][4];
		int drugi[4][4];
		scanf("%d", &row1);
		row1--;
		
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++) scanf("%d ", &prvi[i][j]);
		}
				
		scanf("%d", &row2);
		row2--;
		for (int i = 0; i < N; i++){
			for (int j = 0; j < N; j++) scanf("%d ", &drugi[i][j]);
		}
		
		int eq = 0;
		int ix;
		
		for (int i = 0; i < N; i++){
			for (int j = 0; j < N; j++){
				if (prvi[row1][i] == drugi[row2][j]){
					eq++;
					ix = i;
				}
			}
		}
		if (eq == 0) printf("Case #%d: Volunteer cheated!\n", t+1);
		if (eq > 1) printf("Case #%d: Bad magician!\n", t+1);
		if (eq == 1) printf("Case #%d: %d\n", t+1, prvi[row1][ix]);
	}
	return 0;
}