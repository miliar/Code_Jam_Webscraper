#include <bits/stdc++.h>

using namespace std;

#define FI "A-large.in"
#define FO "out.txt"
const int MAXN = 1e3 + 5;

int T;
int Smax;
int nStand, res;
char info[MAXN];

int main() {
#ifndef ONLINE_JUDGE
	freopen(FI, "r", stdin);
	freopen(FO, "w", stdout);
#endif
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		printf("Case #%d: ", t);
		scanf("%d", &Smax);
		nStand = 0;
		scanf("%s", info);
		res = 0;
		for (int i = 0; info[i] != '\0'; ++i) {
			if (info[i] > '0') {
				if (nStand < i) {
					res += i - nStand;
					nStand = i;
				}
				nStand += info[i] - '0';
			}
		}		
		printf("%d\n", res);
	}	
	return 0;
}
