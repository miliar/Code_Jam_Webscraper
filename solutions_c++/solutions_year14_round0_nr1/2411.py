#include <stdio.h>



int main(){
	int first, second;
	int cas;
	int i, j, k;
	int a[4][4], b[4][4];

	freopen("input.txt","r",stdin);
	freopen("output.txt","w", stdout);
	
	scanf("%d", &cas);
	for (k=1; k<=cas; k++){
		int cnt = 0;
		scanf("%d", &first);
		first--;
		for (i=0; i<4; i++){
			for (j=0; j<4; j++)
				scanf("%d", &a[i][j]);
		}

		scanf("%d", &second);
		second--;
		for (i=0; i<4; i++){
			for (j=0; j<4; j++){
				scanf("%d", &b[i][j]);
			}
		}
		
		
		int l;
		for (i=0; i<4; i++){
			for (j=0; j<4; j++){
				if (a[first][i] == b[second][j]){
					cnt++;
					l = b[second][j];
				}
			}
		}

		if (cnt == 1){
			printf("Case #%d: %d\n", k, l); 	
		}else if (cnt > 1){
			printf("Case #%d: Bad magician!\n", k);
		}else if (cnt == 0){
			printf("Case #%d: Volunteer cheated!\n", k);
		}
	}

	return 0;
}