#include<cstdio>

using namespace std;

int main(void)
{
	int cases;
	int cas;
	double C,F,X;
	double cur;
	double cookies;
	double f;
	double sec1,sec2,tmp;
	scanf("%d",&cases);
	for(cas=1;cas<=cases;cas++)
	{
		cur=f=cookies=0;
		scanf("%lf%lf%lf",&C,&F,&X);
		f=2;
		
		double ans=0;
		while(1)
		{
			//wait
			sec1=(X)/f;
			//buy farm
			tmp=C/f;
			f+=F;
			sec2=X/f+tmp;
			
			if(sec1<sec2) 
			{
				ans+=sec1;
				break;
			}
			else ans+=tmp;

		}
		printf("Case #%d: %.7lf\n",cas,ans);


	}

	return 0;
}
