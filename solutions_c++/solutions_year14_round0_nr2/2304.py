#include <stdio.h>
#include <string.h>
#define print(f,...) printf(f,__VA_ARGS__)
int T;
double C,F,X,res;
int case_num;
int main()
{
	scanf("%d",&T);
	for (case_num = 1; case_num <= T; case_num++)
	{
		print("Case #%d: ",case_num);
		scanf("%lf %lf %lf",&C,&F,&X);
		res=0;
		double income=2;
		while (true)
		{
			double u,v,t;
			u=X/income;
			t=C/income;
			v=t+X/(income+F);
			if (u>v)
			{
				income+=F;
				res+=t;
			}
			else
			{
				res+=u;
				break;
			}
		}
		print("%.7lf\n",res);
	}	
}