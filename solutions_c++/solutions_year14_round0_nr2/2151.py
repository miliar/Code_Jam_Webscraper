#include "cstdio"
int n;
long double c,f,x,k,czas,w,tmp; 
int main()
{
	scanf ("%d", &n);
	for (int i=0; i<n; i++)
	{
		scanf ("%Lf%Lf%Lf", &c, &f, &x);
		
		k=2, tmp=0, czas=0, w=0;
		while (1)
		{
			w=czas+(x/k);
			if (w>tmp && tmp!=0) break;
			
			czas+=(c/k);
			k+=f;
			
			tmp=w;
		}
		printf ("Case #%d: %.7Lf\n", i+1, tmp);
	}
	
	
	return 0;
}