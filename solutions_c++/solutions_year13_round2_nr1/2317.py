#include "cstdio"
#include "algorithm"
using namespace std;
long long n,k,x,p,w,w2,tab[10000005];
int main()
{
	scanf ("%lld", &n);
	
	for (int i=0; i<n; i++)
	{
		scanf ("%lld%lld", &x, &k);
		for (int j=0; j<k; j++) scanf ("%lld", &tab[j]);
		
		if (x==1) w=k;
		else
		{
			sort (tab, tab+k);
			w=0;
			for (p=0; p<k; p++)
			{
				if (x>tab[p]) 
				{
					//printf ("---%lld  oo %lld\n", x, tab[p]);
					x+=tab[p];
				}
				else
				{
					w2=0;
					while (x<=tab[p]) 
					{
						//printf ("---%lld  aa %lld\n", x, tab[p]);
						w2++,x+=(x-1);
					}
					x+=tab[p];
					
					if (w2<(k-p)) w+=w2;
					else
					{
						w+=(k-p);
						break;
					}
					/*
					if ((x*2-1)>tab[p]) x*=2,x--;
					else 
					{
						w+=(k-(p+1));
						break;
					}
					*/
				}
			}
		}
		printf ("Case #%d: %lld\n", i+1, w);
	}
	
	
	return 0;
}
