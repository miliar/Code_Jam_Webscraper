#include<bits/stdc++.h>

using namespace std;

int main()
{
	//freopen("input.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int t,n,a[1010],sum,ans,ind=0;
	char s[1010];
	scanf("%d",&t);
	while(t--)
	{
		ind++;
		scanf("%d",&n);
		scanf("%s",&s);
		sum=0;
		ans=0;
		for(int i=0;i<=1000;i++)	a[i]=0;
		for(int i=0;i<=n;i++)
		{
			a[i]+=s[i]-'0';
		}
		for(int i=0;i<=n;i++)
		{
			if(sum>=i)
			{
				sum+=a[i];
			}
			else if(a[i]>0)
			{
				ans+=(i-sum);
				sum+=(i-sum);
				sum+=a[i];
			}
		}
		printf("Case #%d: %d\n",ind,ans);
	}
	return 0;
}

