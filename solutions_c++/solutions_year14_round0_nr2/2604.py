#include <cstdio>

long double C,F,X,S,IMK;
int ss;

int main()
{
	scanf("%d",&ss);
	for(int s=1;s<=ss;++s)
	{
		printf("Case #%d: ",s);
		scanf("%Lf %Lf %Lf",&C,&F,&X);
		IMK=2.0; S=0;
		while(X/IMK > X/(IMK+F)+(C/IMK))
		{
			S+=C/IMK;
			IMK+=F;
		}
		printf("%.7Lf\n",S+(X/IMK));
	}
	return 0;
}
