#include <cstdio>
int a[5][5], b[5][5];
int main() {
	//freopen("in", "r", stdin);
	//freopen("out", "w", stdout);
	int T, p, q, cases = 0;
	scanf("%d", &T);
	while(T--) {
		printf("Case #%d: ", ++cases);
		scanf("%d", &p);
		for(int i = 1; i <= 4; i++)
			for(int j = 1; j <= 4; j++) 
				scanf("%d", &a[i][j]);
		scanf("%d", &q);
		for(int i = 1; i <= 4; i++)
			for(int j = 1; j <= 4; j++) 
				scanf("%d", &b[i][j]);
		int cnt = 0, ans = 0;
		for(int i = 1; i <= 4; i++)
			for(int j = 1; j <= 4; j++)
				if(a[p][i] == b[q][j]) {
					cnt++;
					ans = a[p][i];
				}
		if(cnt == 0) printf("Volunteer cheated!\n");
		if(cnt > 1) printf("Bad magician!\n");
		if(cnt == 1) printf("%d\n", ans);
	}
	return 0;
}

