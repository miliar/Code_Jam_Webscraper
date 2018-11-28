#include <cstdio>

int t, a, b, k;

int main(void)
{
#ifdef _CONSOLE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);
#endif

	scanf("%d", &t);
	for(int pr=1 ; pr<=t ; pr++)
	{
		int sol=0;
		scanf("%d%d%d", &a, &b, &k);
		for(int i=0 ; i<a ; i++)
		{
			for(int j=0 ; j<b ; j++)
			{
				int and=i&j;
				if(and<k) sol++;
			}
		}
		printf("Case #%d: %d\n", pr, sol);
	}
}