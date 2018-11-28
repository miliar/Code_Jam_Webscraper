#include<bits/stdc++.h>
#define ll long long
#define N 1000000007
#define maxs 100005
#define mins 1005
#define pb push_back
using namespace std;

int a[maxs];
int main()
{
	int t;
	int cnt=1;
	int i,j,k,max1,max2,ans1,ans2,n,max3,val1,ans3,val2;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
		}
		max1=a[0]-a[1];
		max3=a[0];
		for(i=1;i<n;i++)
		{
			max1=max(max1,a[i-1]-a[i]);
			max3=max(max3,a[i]);
		}
		ans1=0;
		for(i=1;i<n;i++)
		{
			if(a[i]<a[i-1])
			{
				ans1+=a[i-1]-a[i];
			}
		}

		if(max1>0)
		{
			ans3=INT_MAX;
			for(i=1;i<=max3;i++)
			{
				ans2=0;
				val1=a[0];
				for(j=1;j<n;j++)
				{
					val2=min(i,val1);
					val1-=val2;
					if(val1>a[j])
					{
						ans2=INT_MAX;
						break;
					}
					val1=a[j];
					ans2+=val2;
				}
			//	cout<<ans2<<" ";
				ans3=min(ans3,ans2);
			}
		}
		else
		{
			ans3=0;
		}
		printf("Case #%d: %d %d\n",cnt,ans1,ans3);
		cnt++;
	}
	return 0;
}
