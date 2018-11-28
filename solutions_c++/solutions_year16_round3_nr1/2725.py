
#include <iostream>

using namespace std;

int main() {
	int t;

	scanf("%d", &t);

	for(int i = 1; i <= t; ++i) {
		int n;
		int num[26] = {0};
		scanf("%d", &n);
		for(int j = 0; j < n; ++j)
			scanf("%d", &num[j]);

		int max1 = 0, max2 = 0, mj1 = -1, mj2 = -1;
		for(int j = 0; j < n; ++j) {
			if(num[j] > max1) {
				mj2 = mj1;
				mj1 = j;
				max2 = max1;
				max1 = num[j];
			}
			else if(num[j] == max1) {
				mj2 = j;
				max2 = num[j];
			}
			else if(num[j] > max2) {
				mj2 = j;
				max2 = num[j];
			}
		}
		printf("Case #%d: ", i);
		while(max1 - max2 != 0) {
			if(max1 - max2 >= 2) {
				num[mj1] -= 2;
				max1 -= 2;
				printf("%c%c ", 'A'+mj1, 'A'+mj1);
			}
			else if(max1 - max2 > 0) {
				num[mj1] --;
				max1 --;
				printf("%c ", 'A'+mj1);
			}
		}

		for(int j = 0; j < n; ++j) {
			if(j == mj1 || j == mj2)
				continue;
			while(num[j] > 0) {
				if(num[j] >= 2) {
					num[j] -= 2;
					printf("%c%c ", 'A' + j, 'A' + j);
				}
				else {
					num[j] --;
					printf("%c ", 'A' + j);
				}
			}
		}
		
		while(max1 > 0) {
			num[mj1] --;
			num[mj2] --;
			max1 --;
			max2 --;
			printf("%c%c ", 'A' + mj1, 'A' + mj2);
		}
		printf("\n");
	}

	return 0;
}
