#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;
int main()
{
 	int t,i;
	long long int r,total,ans,count,K=1;
	//long double pie=3.141592653589793238462643383279,r,t;
	scanf("%d",&t);
	while(t--)
	{
		count=1;
		scanf("%lld%lld",&r,&total);
		total=total-((r+1)*(r+1)-r*r);
		//printf("%lld ",total);
		r=r+2;
		i=3;
		while(total>=0)
		{
			total=total-((r+1)*(r+1)-r*r);
			//printf("%lld ",total);
			count++;
			r=r+2;
		}
		printf("Case #%lld: %lld\n",K,count-1);
		K++;
	}

	return 0;
}
