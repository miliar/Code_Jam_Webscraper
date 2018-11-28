#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	long long aux;
	int bitm, cmp, n;
	
	scanf("%d", &t);
	
	for(int k = 0; k < t; k++)
	{
		scanf("%d", &n);
		
		cmp = (1<<10) - 1;
		
		if(n == 0)
		{
			printf("Case #%d: INSOMNIA\n", k+1);
		}
		
		else
		{
			bitm = 0;
			int m;
			for(m = 1; bitm != cmp; m++)
			{
				aux = n* m;
				//printf("%lld\n", aux);
				
				while(aux > 0)
				{
					bitm |= (1<<aux%10);
					aux /= 10;
				}
			}
			
			aux = (m-1) * n;
			printf("Case #%d: %lld\n", k+1, aux);
			
		}
	}
}
