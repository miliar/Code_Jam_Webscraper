#include"stdio.h"
#include"stdlib.h"
#include"algorithm"
using namespace std;
typedef long long LL;
typedef pair<int, int> II;
int t, T, R, C, nR[105][105], nC[105][105];
char str[105][105];
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.txt", "w", stdout);
	scanf("%d", &T);
	while (t < T) {
		scanf("%d%d", &R, &C);
		for (int i = 1; i <= R; i++) {
			scanf("%s", &str[i][1]);
			for (int j = 1; j <= C; j++) {
				nR[i][j] = nR[i-1][j];
				nC[i][j] = nC[i][j-1];
				if (str[i][j] == '.') continue;
				nR[i][j]++; nC[i][j]++;
			}
		}
		bool noAns = false;
		int Ans = 0;
		for (int i = 1; !noAns && i <= R; i++)
			for (int j = 1; !noAns && j <= C; j++) {
				if (str[i][j] == '.') continue;
				if (nR[R][j] == 1 && nC[i][C] == 1) {
					noAns = true;
					break;
				}
				int dir = 0, ok = 0;
				switch (str[i][j]) {
					case '>': dir = 0; 
						if (nC[i][C] - nC[i][j] > 0) ok = 1;
						break;
					case 'v': dir = 1; 
						if (nR[R][j] - nR[i][j] > 0) ok = 1;
						break;
					case '<': dir = 2;
						if (nC[i][j-1] > 0) ok = 1;
						break;
					case '^': dir = 3;
						if (nR[i-1][j] > 0) ok = 1;
						break;
				}
				if (!ok) Ans++;
			}
		printf("Case #%d: ", ++t);
		if (noAns) printf("IMPOSSIBLE\n");
		else printf("%d\n", Ans);
	}
}
