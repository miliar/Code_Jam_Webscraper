#include "cstdio"
int t,n,k,w;
char s[1005];
int main()
{
	scanf ("%d", &t);
	for (int v=1; v<=t; v++)
	{
		scanf ("%d %s", &n, s);
		k=0,w=0;
		for (int i=0; i<=n; i++)
		{
			if (k<i)
			{
				w+=(i-k);
				k+=(i-k);
			}
			k+=s[i]-48;
		}
		printf ("Case #%d: %d\n", v, w);
	}
	
	return 0;
}