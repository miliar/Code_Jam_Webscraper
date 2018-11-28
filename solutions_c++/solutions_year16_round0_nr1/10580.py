#include "cstdio"
long long t,n,m,k,p,w;
bool odw[15];
int main()
{
	scanf ("%lld", &t);
	
	for (int y = 1; y <= t; y++)
	{
		scanf ("%lld", &n);
		m = n;
		k = 0;
		for (int i = 0 ; i < 10; i++) odw[i] = false;
		
		if (n != 0)
		{
			for (int i = 2 ; i < 1000002; i++)
			{
				p = n;
				while (p > 0)
				{
					if (!odw[p % 10])
					{
						odw [p % 10] = true;
						k++;
					}
					
					p /= 10;
				}
				
				if (k == 10)
				{
					w = n;
					break;
				}
				
				n = m * i;
			}
		}
		
		printf ("Case #%d: ", y);
		(k == 10) ? printf ("%lld\n", w) : printf ("INSOMNIA\n");
	}
	
	return 0;
}