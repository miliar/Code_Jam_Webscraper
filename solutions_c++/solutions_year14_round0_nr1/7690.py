#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int arrange[2][4][4];

int main(){
	int T, ans[2];
	scanf("%d", &T);
	int ttt = 0;
	while (T--){
		for (int k = 0; k < 2; k++){
			scanf("%d", ans+k);
			ans[k]--;
			for (int i = 0; i < 4; i++)
				for (int j = 0; j < 4; j++)
					scanf("%d", arrange[k][i]+j);
		}
		int count = 0;
		int result;
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				if (arrange[0][ans[0]][i] == arrange[1][ans[1]][j]){
					count++;
					result = arrange[0][ans[0]][i];
					break;
				}
			}
		}
		printf("Case #%d: ", ++ttt);
		if (count == 1)
			printf("%d\n", result);
		else if (count > 0)
			printf("Bad magician!\n");
		else
			printf("Volunteer cheated!\n");
	}
	return 0;
}