#include <cstdio>
using namespace std;

int main() {
	int T;
	scanf("%d",&T);
	for (int i = 1; i <= T; ++i) {
		int ans1, ans2, card1[5][5], card2[5][5];
		scanf("%d",&ans1);
		for (int j = 1; j <=4 ;++j) {
			for (int k = 1; k <= 4;++k) {
				scanf("%d",&card1[j][k]);
			}
		}
		scanf("%d",&ans2);
		for (int j = 1; j <= 4;++j) {
			for (int k = 1; k <= 4;++k) {
				scanf("%d",&card2[j][k]);
			}
		}
		
		int cnt = 0;
		int angka;
		int arr[17] = {0};
		for (int j = 1; j <= 4;++j) {
			++arr[card1[ans1][j]];
		}
		for (int j = 1; j <= 4;++j) {
			++arr[card2[ans2][j]];
			if (arr[card2[ans2][j]] == 2) {
				if (cnt == 0) {
					++cnt;
					angka = card2[ans2][j];
				} else {
					printf("Case #%d: Bad Magician!\n",i);
					goto end;
				}
			}
		}
		
		if (cnt == 1) 
			printf("Case #%d: %d\n",i,angka);
		else
			printf("Case #%d: Volunteer cheated!\n",i);
		end:
			printf("");
	}
	return 0;
}