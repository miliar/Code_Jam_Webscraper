#include<iostream>
using namespace std;
//---------------------------------------------

int main()
{
//	freopen("B-large.in","r",stdin);
	//freopen("cookie.txt","w",stdout);
	int t;
	cin>>t;
	for(int test=1;test<=t;test++)
	{
		double c,f,x;
		scanf("%lf%lf%lf",&c,&f,&x);
		
		int k=0;
		double time=0.0;
		if(x<=c)
			time=time+x/2;
		else
		{
			while(x*((k)*f+2) < (x-c)*((k+1)*f+2))
			{
				time=time+c/((k)*f+2);
				k++;
			}
			time=time+x/(k*f+2);
		}
		printf("Case #%d: %.7f\n",test,time);
	}
}
