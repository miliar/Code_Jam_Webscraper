#include <stdio.h>
int maze[5][5];
int main () {
	int T;
//	freopen("A-small-attempt0.in","r",stdin);
//	freopen("As0.out","w",stdout);
	scanf ("%d",&T);
	int cas = 0;
	while (T --) {
		int n,m;
		cas ++;
		scanf ("%d",&n);
		int buf[20] = {0};
		for (int i = 1;i <= 4;i ++) {
			for (int j = 1;j <= 4;j ++) {
				scanf ("%d",&maze[i][j]);
			}
		}
		for (int i = 1;i <= 4;i ++) buf[ maze[n][i] ] ++;
		scanf ("%d",&m);
		for (int i = 1;i <= 4;i ++) {
			for (int j = 1;j <= 4;j ++) {
				scanf ("%d",&maze[i][j]);
			}
		}
		printf("Case #%d: ",cas);
		for (int i = 1;i <= 4;i ++) buf[ maze[m][i] ] ++;
		int cnt = 0;
		int idx = -1;
		for (int i = 1;i <= 16;i ++) {
			if (buf[i] == 2) {
				cnt ++;
				idx = i;
			}
		}
		if (cnt == 0) {
			puts("Volunteer cheated!");
		} else if (cnt == 1) printf("%d\n",idx);
		else puts("Bad magician!");
	}
	return 0;
}