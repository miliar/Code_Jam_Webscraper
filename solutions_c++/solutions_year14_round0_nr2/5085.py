#include <stdio.h>
 
int main()
{
	int t, i=1;
    double cp=2, c, f, x, sec=0;
	scanf("%d", &t);
	while(t--)
	{
		sec=0;
		cp=2;
		scanf("%lf %lf %lf",&c,&f,&x);
		while(1)
		{
			if(((c/(cp))+(x/(cp+f)))>(x/cp))
			{
				printf("Case #%d: %.7lf\n", i, (sec+(x/cp)));
				i++;
				break;
			}
			else
			{
				sec+=(c/cp);
				cp+=f;
			}
		}
	}
	return 0;
}
