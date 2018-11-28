#include<cstdlib>
#include<cstdio>
#include<iostream>
using namespace std;
int main()
{
	int t,n,cal,ans;
	register int i=0,j=0;
	char s[1005];
	scanf("%d",&t);
	while(t--)
	{
		j++;
		cal=ans=0;
		scanf("%d%s",&n,s);
		cal+=s[0]-'0';
		for(i=1;i<=n;i++)
		{
			if(cal<i)
			{
				ans+=i-cal;
				cal=i;
			}
			cal+=s[i]-'0';
		}
		cout<<"Case #"<<j<<": "<<ans<<endl;
	}
	return 0;
}
