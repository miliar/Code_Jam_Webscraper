#include <stdio.h>
#include <string.h>
int main()
{
	int t;
	int a[4][4];
	int b[4][4];
	int line1, line2;
	int i;
	int j;
	int k;
	int count;
	int ans;
	scanf("%d", &t);
	for(i = 1; i <= t; i++) {
		scanf("%d", &line1);
		line1--;
		for(j = 0; j < 4; j++) scanf("%d %d %d %d", &a[j][0], &a[j][1], &a[j][2], &a[j][3]);
		scanf("%d", &line2);
		line2--;
		for(j = 0; j < 4; j++) scanf("%d %d %d %d", &b[j][0], &b[j][1], &b[j][2], &b[j][3]);
		count = 0;
		for(j = 0; j < 4; j++) {
			for(k = 0; k < 4; k++) {
				if(a[line1][j] == b[line2][k]) {
					count++;
					ans = a[line1][j];
					break;
				}
			}
		}
		if(count > 1) printf("Case #%d: Bad magician!\n", i);
		else if(count == 1) printf("Case #%d: %d\n", i, ans);
		else printf("Case #%d: Volunteer cheated!\n", i);
	}
	return 0;
}
