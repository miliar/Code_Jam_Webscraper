#include<stdio.h>
using namespace std;

int main(){
	int t,i,j,k,possible;
	double c,f,x,lo,mid,hi,current_rate,making_time;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{	
		scanf("%lf %lf %lf",&c,&f,&x);
		lo=0;
		hi=x/2;
		while(hi - lo > 0.00000001)
		{
			mid = (hi+lo)/2;
			making_time=0;
			possible=0;
			current_rate=2;
			
			for(i=0;i<= x/c +1;i++)
			{
				if((mid-making_time)*(current_rate)>=x)
				{
					possible=1;
					break;
				}
				making_time = making_time + c/current_rate; 
				current_rate = current_rate+f;				
			}
			if(possible==1)
				hi=mid;
			else
				lo=mid;	
		}
		printf("Case #%d: %0.7f\n",k,hi);
	}
}
