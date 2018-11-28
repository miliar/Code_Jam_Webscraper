#include <stdio.h>

int main() {
	int n;
	char map[5][5];

	scanf("%d", &n);

	for(int i = 0; i < n; i++) {

		for(int j = 0; j < 4; j++) {
			scanf("%s", &map[j]);
		}

		int flag = 0;
		int p = 0;

		for(int j = 0; j < 4; j++) {
			int x1 = 0;
			int x2 = 0;
			int x3 = 0;
			int x4 = 0;
			int o1 = 0;
			int o2 = 0;
			int o3 = 0;
			int o4 = 0;
			int t1 = 0;
			int t2 = 0;
			int t3 = 0;
			int t4 = 0;

			for(int k = 0; k < 4; k++) {
				
				switch(map[j][k]) {
				case 'X' :
					x1++;
					break;
				case 'O' :
					o1++;
					break;
				case 'T' :
					t1++;
					break;
				case '.' :
					p++;
					break;
				default :
					break;
				}

				switch(map[k][j]) {
				case 'X' :
					x2++;
					break;
				case 'O' :
					o2++;
					break;
				case 'T' :
					t2++;
					break;
				case '.' :
					p++;
					break;
				default :
					break;
				}

				switch(map[k][k]) {
				case 'X' :
					x3++;
					break;
				case 'O' :
					o3++;
					break;
				case 'T' :
					t3++;
					break;
				case '.' :
					p++;
					break;
				default :
					break;
				}

				switch(map[k][3-k]) {
				case 'X' :
					x4++;
					break;
				case 'O' :
					o4++;
					break;
				case 'T' :
					t4++;
					break;
				case '.' :
					p++;
					break;
				default :
					break;
				}
			}

			if(x1 == 4 || (x1 == 3 && t1 == 1) || x2 == 4 || (x2 == 3 && t2 == 1)
				|| x3 == 4 || (x3 == 3 && t3 == 1) || x4 == 4 || (x4 == 3 && t4 == 1)) {
				printf("Case #%d: X won\n", i+1);
				flag = 1;
				break;
			}
			else if(o1 == 4 || (o1 == 3 && t1 == 1) || o2 == 4 || (o2 == 3 && t2 == 1)
				|| o3 == 4 || (o3 == 3 && t3 == 1) || o4 == 4 || (o4 == 3 && t4 == 1)) {
				printf("Case #%d: O won\n", i+1);
				flag = 1;
				break;
			}
		}

		if(flag == 0 && p == 0) {
			printf("Case #%d: Draw\n", i+1);
		}
		else if(flag == 0 && p > 0) {
			printf("Case #%d: Game has not completed\n", i+1);
		}
	}

	return 0;
}