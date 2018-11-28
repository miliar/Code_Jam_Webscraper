#include <stdio.h>

int main()
{
	int tc;
	int cnt = 0;
	scanf("%d", &tc);
	while(cnt++ < tc){
		int a[2][4][4];
		int x[2];
		int i, j, k;
		for(k = 0; k < 2; k++){
			scanf("%d", &x[k]);
			for(i = 0; i < 4; i++){
				for(j = 0; j < 4; j++){
					scanf("%d", &a[k][i][j]);
				}
			}
		}
		int ans = 0;
		for(i = 0; i < 4; i++){
			for(j = 0; j < 4; j++){
				if(a[0][x[0] - 1][i] == a[1][x[1] - 1][j]){
					if(ans != 0) break;
					ans = a[0][x[0] - 1][i];
				}
			}
			if(j != 4) break;
		}
		printf("Case #%d: ", cnt);
		if(j != 4) printf("Bad magician!\n");
		else if(ans == 0) printf("Volunteer cheated!\n");
		else printf("%d\n", ans);
	}
	return 0;
}