#include <stdio.h>
#include <algorithm>

using namespace std;

int tst, n;
int P[1009], ans, sol;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	
	scanf("%d" ,&tst);
	
	for (int t=1; t<=tst; t++)
	{
		scanf("%d" ,&n);
	
		ans = 1000000000;
		
		for (int i=0; i<n; i++)
			scanf("%d" ,&P[i]);
		
		for (int j=1; j<=1000; j++)
		{
			sol = j;
			
			for (int i=0; i<n; i++)
				sol += (P[i]-1)/j;
			
			ans = min(ans, sol);
		}
		
		printf("Case #%d: %d\n" ,t ,ans);
	}
}
