#include <stdio.h>
 
int main() 
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d",&T);
	for (int i=1; i<=T; i++) {
		int ret=1e9;
		int d,P[1010]={0};
		scanf("%d",&d);
		for (int j=1; j<=d; j++) {
			scanf("%d", P+j);
		}

		for (int j=1; j<=1000; j++) {
			int ans = j;
			for (int k=1; k<=d; k++) {
				if (P[k] > j) {
					ans += P[k]/j - !(P[k]%j);
				}
			}
			if (ret > ans) { ret = ans; }
		}

		printf("Case #%d: %d\n",i, ret);
	}



}