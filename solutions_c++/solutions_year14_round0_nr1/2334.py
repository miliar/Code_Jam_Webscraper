#include<stdio.h>

int pre[5][5], next[5][5];

int main() {

	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);

	int pre_row, next_row, T, cnt, ans, num=1;
	int i,j;

	scanf("%d", &T);
	while(T-- > 0) {
		scanf("%d", &pre_row);
		for(i=0 ; i<4 ; i++) for(j=0 ; j<4 ; j++) scanf("%d", &pre[i][j]);
		scanf("%d", &next_row);
		for(i=0 ; i<4 ; i++) for(j=0 ; j<4 ; j++) scanf("%d", &next[i][j]);

		for(i=0,cnt=0 ; i<4 ; i++) {
			for(j=0 ; j<4 ; j++) {
				if(pre[pre_row-1][i] == next[next_row-1][j]) {cnt++; ans=pre[pre_row-1][i]; }
			}
		}

		printf("Case #%d: ", num++);
		if(cnt == 0) printf("Volunteer cheated!\n");
		else if(cnt == 1) printf("%d\n", ans);
		else printf("Bad magician!\n");
	}

	return 0;
}