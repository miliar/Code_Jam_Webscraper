#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
const int maxn = 1000005;
char str[maxn];
long long ans;
long long dp[maxn];
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int cas,n,len;
	scanf("%d",&cas);
	memset(dp,0,sizeof(dp));
	for(int ca = 1; ca <= cas; ca++)
	{
		scanf("%s%d",str,&n);
		ans = 0;
		len = strlen(str);
		int l=0,cnt=0,x=0;
		for(int i = 0; str[i];i++)
		{
			cnt = 0;
			for(int j = i; j < len; j++)
			{
				if(str[j]=='a'||str[j]=='e'||str[j]=='i'||str[j]=='u'||str[j]=='o')
				{
					cnt = 0;
				}
				else cnt++;
				if(cnt>=n)
				{
					ans+=len-j;
					break;
				}
			}
		}

		printf("Case #%d: %lld\n",ca,ans);
	}
	return 0;
}
