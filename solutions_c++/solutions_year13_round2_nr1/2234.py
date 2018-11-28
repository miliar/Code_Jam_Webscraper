#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cstdlib>
using namespace std;
typedef int LL;

LL arr[103];
int main()
{
	LL t,cas=0,A,n,sum,i,ans,cnt,sum1;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&A,&n);
		for(i=1;i<=n;i++)
		{
			scanf("%d",&arr[i]);
		}
		if(A==1)
		{
			printf("Case #%d: %d\n",++cas,n);
			continue;
		}
		sort(arr+1,arr+n+1);
		sum=A;
		ans=0;
		for(i=1;i<=n;i++)
		{
			if(sum>arr[i])
			{
				sum+=arr[i];
				if(sum>arr[n]){break;}
				continue;
			}
			sum1=sum;
			cnt=0;
			while(sum1<=arr[i])
			{
				sum1+=sum1-1;
				cnt++;
			}
			if(cnt>=n-i+1)
			{
				ans+=n-i+1;
				break;
			}
			ans+=cnt;
			sum=sum1+arr[i];
			if(sum>arr[n]){break;}
		}
		printf("Case #%d: %d\n",++cas,ans);
	}
	return 0;
}