#include <cstdio>
int q1[5][5], q2[5][5];

int main(){
	freopen("in.txt", "r", stdin);
	freopen("A-small-attempt0.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; tt++){
		int n;
		scanf("%d", &n);
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				scanf("%d", &q1[i][j]);
			}
		}
		int m;
		scanf("%d", &m);
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				scanf("%d", &q2[i][j]);
			}
		}

		int ans = 0, p;
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				if (q1[n - 1][i] == q2[m - 1][j]) {
					ans++; p = q1[n - 1][i];
				}
			}
		}

		if (ans == 1) printf("Case #%d: %d\n", tt, p);
		else if (ans) printf("Case #%d: Bad magician!\n", tt);
		else printf("Case #%d: Volunteer cheated!\n", tt);
	}
}