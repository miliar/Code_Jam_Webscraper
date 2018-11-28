#include <iostream>
#include <cstdio>
#include <cassert>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("data.out","w",stdout);
	int T;
	double M=2.0;
	double result=0;
	double C,F,X;
	double t1,t2;
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		scanf("%lf%lf%lf",&C,&F,&X);
	//	printf("%f %f %f\n",C,F,X);
		result=0;
		M=2.0;
		if(C>=X)
		{
			result=X/M;
		}
		else
		{
	
			t1=(X-C)/M;//bu xiu farm
			t2=X/(M+F);
			while(t1>t2)
			{
				result+=C/M;
				M=M+F;
			
				t1=(X-C)/M;//bu xiu farm
				t2=X/(M+F);
			}
			result+=X/M;
		}
		printf("Case #%d: %.7lf\n",i+1,result);
		
	}

	return 0;
}


