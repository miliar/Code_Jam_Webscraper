#include<cstdio>
#include<algorithm>
using namespace std;

int t, cn;
char str[100][101];

int main() {
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	scanf("%d", &t);
	for (cn=1; cn<=t; cn++) {
		int n;
		scanf("%d", &n);
		for (int i=0; i<n; ++i)
			scanf(" %s", str+i);
		printf("Case #%d: ", cn);
		int ans = 100000, possible = 1;
		for (int p=0; p<n; ++p) {
			int res = 0;
			for (int i=0; i<n; ++i) {
				int idxp = 0, idxi = 0;
				while(str[p][idxp] || str[i][idxi]) {
					if (str[p][idxp] != str[i][idxi]) {
						possible = 0; break;
					}
					if (str[p][idxp+1] == str[p][idxp]) {
						++idxp;
						if (str[i][idxi+1] == str[i][idxi])
							++idxi;
						else
							++res;
					} else if (str[i][idxi+1] == str[i][idxi]) {
						++idxi;
						++res;
					} else {
						++idxp;
						++idxi;
					}
				}
				if (!possible) break;
			}
			if (!possible) break;
			ans = min(ans, res);
		}
		if (possible)
			printf("%d\n", ans);
		else
			printf("Fegla Won\n");
	}
	return 0;
}