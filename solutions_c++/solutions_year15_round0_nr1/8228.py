#include <cstdio>
#include <cstring>
using namespace std;
int main()
{
	#ifdef CLMAN
		freopen("input.in", "r", stdin);
		freopen("output.out", "w", stdout);
	#endif // CLMAN
	int tc,smax,cnt,csn,ans;
	char s[1005];
	while(scanf("%d",&tc)==1)
	{
		csn=0;
		while(tc--)
		{
			cnt=0;ans=0;
			scanf("%d",&smax);
			scanf("%s",s);
			for(int i=0;i<=smax;i++)
			{
				if(cnt<i)
				{
					ans+=(i-cnt);
					cnt+=(i-cnt);
				}
				cnt+=(s[i]-'0');
			}
			printf("Case #%d: %d\n",++csn,ans);
		}
	}
	return 0;
}
