#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;


int a[11234];
bool in[11234];


int
main(void)
{
	int t;
	scanf("%d", &t);
	for(int T = 1; T <= t; T++)
	{
		memset(in, 0, sizeof(in));
		int n, m, ans = 0;
		scanf("%d %d", &n, &m);
		for(int i = 0; i < n; i++)
			scanf("%d", &a[i]);
		sort(a, a+n);
		for(int i = n-1; i >= 0; i--)
		{
			if(!in[i])
			{
				ans++;
				in[i] = true;
				int x = -1;
				for(int j = 0; j < i; j++)
					if(!in[j] && a[j] <= m - a[i])
						x = j;
				if(x!= -1)
					in[x] = true;
			}
		}
		printf("Case #%d: %d\n", T, ans);
	}
}
