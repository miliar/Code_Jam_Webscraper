#include<bits/stdc++.h>
using namespace std;
char a[1005];
int main()
{
	int t,s,n,cnt,sum,k,z=1;
	freopen("A-large.in","r",stdin);
	freopen("first.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&s);
		scanf("%s",&a);
		n=s+1,cnt=0,sum=0;
		for(int i=0;i<n;i++)
		{
		k=a[i]-'0';
		if(k>0)
		{
		if(sum<i)
		{
			cnt+=(i-sum);
			sum=i+k;
		}
		else
		sum+=k;
		}
		}
		printf("Case #%d: %d\n",z++,cnt);
	}
	return 0;
}
