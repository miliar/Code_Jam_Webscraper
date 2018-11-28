#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<map>
#include<cmath>
using namespace std;
int n;
char s[1005];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("data.out","w",stdout);
	int i,t,cnt,ca=1,ans;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		scanf("%s",s);
		ans=0;cnt=0;
		if(s[0]=='0')
		cnt=ans=1;
		else
		cnt=s[0]-'0';
		for(i=1;i<=n;i++)
		{
			if(i>cnt)
			{
				ans+=(i-cnt);
				cnt=i;
			}
			cnt+=(s[i]-'0');
		}
		printf("Case #%d: %d\n",ca++,ans);
	}
	return 0;
}
