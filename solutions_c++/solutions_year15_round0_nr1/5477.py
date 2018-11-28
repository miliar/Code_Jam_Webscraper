#include<bits/stdc++.h>
using namespace std;
int main()
{
	int tc,n,i,ans,base,j;
	char str[1003];
	scanf("%d",&tc);
	for(j=1;j<=tc;j++)
	{
		scanf("%d%s",&n,str);
		ans=0;
		base=str[0]-'0';
		for(i=1;i<=n;i++)
		{
			if(base>=i)
			{
				base+=str[i]-'0';
			}
			else
			{
				ans+=i-base;
				base=i+str[i]-'0';
			}

		}
		printf("Case #%d: %d\n",j,ans);

	}
	return 0;
}