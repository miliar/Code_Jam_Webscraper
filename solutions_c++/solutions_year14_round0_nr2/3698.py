#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
    freopen ("B-large.in","r",stdin);
	freopen ("out.in","w",stdout);
    double C,F,X,start,x1,x2,x3,res_time;
	int t,k=1;
	scanf("%d",&t);
    while(k<=t)
	{
		scanf("%lf %lf %lf",&C,&F,&X);
		start=2; 
        res_time=0;
		while(1)
		{
			x1=X/start;
			x2=start+F;
			x3=(X/x2) + (C/start);
			if(x3<x1)
			res_time+=(C/start);
			else
			{
				res_time+=(X/start);
				break;
			}
			start+=F;
		}
		printf("Case #%d: ",k);
		printf("%.07f\n",res_time);
	k++;
    }
	//system("pause");
	return 0;
}
