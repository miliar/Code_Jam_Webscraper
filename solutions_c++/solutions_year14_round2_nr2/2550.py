#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;


int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	int T, A, B, K;
	int idx = 0;
	scanf("%d", &T);
	while(idx ++ < T)
	{
		int tot = 0;
		scanf("%d %d %d", &A, &B, &K);
		for(int i = 0; i < A; i ++)
		{
			for(int j = 0; j < B; j ++)
			{
				if((i & j) < K)
					tot += 1;
			}
		}
		printf("Case #%d: %d\n", idx, tot); 
	}
}

