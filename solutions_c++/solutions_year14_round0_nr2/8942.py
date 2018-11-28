#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
	freopen("ain.txt","r",stdin);
	freopen("aout.txt","w",stdout);
	double c,f,x,rate,tm,y,ans,w,p;
	int t;
	scanf("%d",&t);
	for(int k=1;k<=t;k++)
	{
		rate=2;tm=0;y=0;
		scanf("%lf%lf%lf",&c,&f,&x);
		
		ans=x;
		while(1)
		{
			if(x>=y)
			{
			
			w=(x-y)/rate;
			
			
			
			//printf("w=%f\n",ans);
			if(ans>(tm+w))
			ans=tm+w;
			else
			break;
			
			}
			else 
			break;
			if(c>=y&&c<x)
			{

			p=(c-y)/rate;
			y+=rate*p;
			y-=c;
			tm+=p;
			rate+=f;
			
			}
		}
		printf("Case #%d: %0.7lf\n",k,ans);
		
	}
}
