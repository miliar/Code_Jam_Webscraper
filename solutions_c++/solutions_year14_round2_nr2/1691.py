#include <stdio.h>

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	
	int T;
	scanf("%d", &T);
	
	for(int t = 1; t <= T; t++)
	{
		int a, b, k, count = 0;
		scanf("%d %d %d", &a, &b, &k);
		
		for(int i = 0; i < a; i++)
			for(int j = 0; j < b; j++)
				if((i & j) < k)
					count++;
		
		printf("Case #%d: %d\n", t, count);
	}
	return 0;
}

