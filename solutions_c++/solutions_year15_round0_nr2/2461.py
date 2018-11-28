#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
	freopen ("aaa.in", "r", stdin);
   freopen ("output.txt", "w", stdout);
	int t,n,a[100000],i,res,ans,v=0,count,max,temp;
	scanf("%d",&t);
	while(t--)
	{
		v++;  ;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
		}
		sort(a,a+i);
		max=a[n-1];
		ans=max;
		for(i=1;i<=max;i++)
		{
			temp=i;
			
             for(int j=0;j<n;j++)
             {
                 if(a[j]>i)
                  {
                    if( a[j]%i == 0 )
                    {
					   temp=temp+(a[j]/i-1);
					}
                    else
                     {
					 temp=temp+(a[j]/i);
					 }
                  }
                     
             }
             ans=min(ans,temp);
		}
		
			printf("Case #%d: %d\n",v,ans);
	   }
	
	
	return 0;
}
