#include <cstdio>


int main()
{
	int t;
	long double c,f,x,ans,aux,cps=2,t1,t2;
	scanf("%i",&t);
	for(int i=1;i<=t;i++)
	{
		cps=2;
		ans=0;
		scanf("%Lf",&c);
		scanf("%Lf",&f);		
		scanf("%Lf",&x);
		bool quit=false;
		if (c >= x) ans=x/2;
		else while (not(quit))
		{
			t1=c/cps;
			t2=x/cps;
			cps=cps+f;
			if (t1+x/cps >= t2){
				ans=ans+t2;
				quit=1;
			}
			else
			{
				ans=ans+t1;
			} 
		}	
		printf("Case #%i: %Lf \n",i,ans);	
	}
	return 0;

}
