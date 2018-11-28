#include <stdio.h>
#include <string.h>
#include <stdlib.h>

const int MAXN = 18;

int hs1[MAXN], hs2[MAXN];

int main(){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int T, r1, r2, x, sum, sum_i;
	scanf("%d", &T);
	for (int cases = 1; cases <= T; ++cases){
		memset(hs1, 0, sizeof(hs1));
		memset(hs2, 0, sizeof(hs2));

		scanf("%d", &r1);
		for (int i = 1; i <= 4; ++i){
			for (int j = 1; j <= 4; ++j){
				scanf("%d", &x);
				if (r1 == i) ++hs1[x];
			}
		}

		scanf("%d", &r2);
		for (int i = 1; i <= 4; ++i){
			for (int j = 1; j <= 4; ++j){
				scanf("%d", &x);
				if (r2 == i) ++hs2[x];
			}
		}

		sum = 0;
		sum_i = -1;
		for (int i = 1; i <= 16; ++i){
			if (hs1[i] && hs2[i]){
				sum++;
				sum_i = i;
			}
		}
		if (sum == 1) printf("Case #%d: %d\n", cases, sum_i);
		else if (sum == 0) printf("Case #%d: %s\n", cases, "Volunteer cheated!");
		else printf("Case #%d: %s\n", cases, "Bad magician!");
	}
	return 0;
}
