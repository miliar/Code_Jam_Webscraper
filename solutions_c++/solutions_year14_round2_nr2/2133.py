#include "bits/stdc++.h"

int main(int argc, char const *argv[])
{
	int T,A,B,K,c,cnt;
	scanf("%d", &T);
	c = 1;
	while(T--){
		cnt = 0;
		scanf("%d %d %d", &A, &B, &K);
		for (int i = 0; i < A; i++){
			for (int j = 0; j < B; ++j)
			{
				if ((i  & j) < K) cnt++;
			}
		}
		printf("Case #%d: %d\n", c++, cnt);
	}
	return 0;
}