#include <bits/stdc++.h>
using namespace std;
int solve(int card1[][4],int card2[][4], int a, int b)
{
	int ans;
	int cn = 0;
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (card2[b][i] == card1[a][j]) {
				cn++;
				ans = card1[a][j];
				break;
			}
		}
	}
	if (cn == 0) return -1;
	if (cn > 1) return 0;
	return ans;
}
int main()
{
	int t;
	scanf("%d",&t);
	int cs = 1;
	while (t--) {
		int a,b;
		int card1[4][4];
		int card2[4][4];
		scanf("%d",&a);
		a--;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				scanf("%d",&card1[i][j]);
			}
		}
		scanf("%d",&b);
		b--;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				scanf("%d",&card2[i][j]);
			}
		}
		int ans = solve(card1,card2,a,b);
		printf("Case #%d: ",cs++);
		if (ans == -1) {
			printf("Volunteer cheated!\n");
		}
		else if (ans == 0) {
			printf("Bad magician!\n");
		}
		else {
			printf("%d\n",ans);
		}
	}
	return 0;
}
