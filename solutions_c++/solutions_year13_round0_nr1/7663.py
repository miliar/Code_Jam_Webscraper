#include <stdio.h>

int main()
{
	int T, t;
	scanf("%d", &T);
	for (t=1;t<=T;t++) {
		char map[4][5];
		int total = 0;
		for (int i=0;i<4;i++) {
			scanf("%s", map[i]);
			for (int j=0;j<4;j++) 
				total += map[i][j];
		}
		int end = 0;
		if (end ==0 ) {
		for (int i=0;i<4;i++) {
			int sum = 0;
			for (int j=0;j<4;j++)
				sum += map[i][j];
			if (sum == 348 || sum == 352) {
				printf("Case #%d: X won\n", t);
				end =1 ;
				break;
			} else if (sum == 316 || sum == 321 ) {
				printf("Case #%d: O won\n", t);
				end =1 ;
				break;
			}
		}
		}
		if (end==0) {
		for (int i=0; i<4;i++) {
			int sum = 0;
			for (int j=0;j<4;j++)
				sum += map[j][i];
			if (sum == 348 || sum == 352) {
				printf("Case #%d: X won\n", t);
				end =1 ;
				break;
			} else if (sum == 316 || sum == 321 ) {
				printf("Case #%d: O won\n", t);
				end =1 ;
				break;
			}
		}
		}
		if (end ==0 ) {
		int sum = 0;
		for (int i=0;i<4;i++)
			sum += map[i][i];
			if (sum == 348 || sum == 352) {
				printf("Case #%d: X won\n", t);
				end =1 ;
			} else if (sum == 316 || sum == 321 ) {
				printf("Case #%d: O won\n", t);
				end =1 ;
			}
		}
		if (end ==0) {
		int sum = 0;
		for (int i=0;i<4;i++)
			sum += map[i][3-i];
			if (sum == 348 || sum ==352) {
				printf("Case #%d: X won\n", t);
				end =1 ;
			} else if (sum == 316 || sum ==321 ) {
				printf("Case #%d: O won\n", t);
				end =1 ;
			}
		}

		if (end ==0) {
			if (total < 1264) 
				printf("Case #%d: Game has not completed\n", t);	
			else
				printf("Case #%d: Draw\n", t);
		}
	}
	return 0;
}
		





