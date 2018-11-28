#include "cstdio"
int main()
{
	int n,a,b,w;
	scanf ("%d", &n);
	
	for (int i=0; i<n; i++)
	{
		scanf ("%d%d", &a, &b);
		
		printf ("Case #%d: ", i+1);
		w=0;
		if (a<=1 && b>=1) w++;
		if (a<=4 && b>=4) w++;
		if (a<=9 && b>=9) w++;
		if (a<=121 && b>=121) w++;
		if (a<=484 && b>=484) w++;
		printf ("%d\n", w);
	}
	
	return 0;
}
