#include<stdio.h>
#include<stdlib.h>
#include<set>
#include<vector>
#include<list>
#include<stack>
#include<map>
#include<math.h>

using namespace std;
typedef unsigned long long  uli;

uli search(uli tt,uli tr,uli min,uli max)
{
	if(max<min)
		return max;
	uli mid=(min+max)/2;
	long double against=(tt+mid)/mid;
	uli check=2*(mid+tr);
	if(check < against)
		return search(tt,tr,mid+1,max);
	else if(check > against)
		return search(tt,tr,min,mid-1);
	return mid;
}
int main()
{
	int i,t;
	uli r,tt,n;
	long double value;
	freopen("ain.txt","r",stdin);
	freopen("aout.txt","w",stdout);
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{	
		printf("Case #%d: ",i);
		scanf("%lld %lld",&r,&tt);
		printf("%lld",search(tt,r,1,tt));
		printf("\n");
	}
	return 0;
}