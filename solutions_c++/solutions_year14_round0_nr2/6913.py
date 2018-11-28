#include<cstdio>

using namespace std;
//%Lf
int main()
{
	freopen("CookieLarge.in","r",stdin);
	freopen("CookieLarge.out","w",stdout);
	int T,cases;
	scanf("%d",&T);
	long double c,f,x;
	
	for(cases=1;cases<=T;cases++)
	{
		long double cr =2.0;
		scanf("%Lf%Lf%Lf",&c,&f,&x);
		printf("Case #%d: ",cases);
		
		long double time = 0.0;
		if(c>=x)
		printf("%.7Lf\n",x/2);
		else
		{
			while(x/cr>(c/cr+(x/(cr+f))))
			{
				time+=c/cr;
				cr=cr+f;
			}
				
			
			
				time+=x/cr;
				printf("%.7Lf\n",time);
			
		}
		
	}
	
}
