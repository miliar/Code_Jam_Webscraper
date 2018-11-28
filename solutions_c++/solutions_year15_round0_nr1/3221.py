#include <stdio.h>
#include <string.h>
using namespace std;
int main(int argc, char const *argv[])
{
	int t,n,ans,cnt;
	char str[2000];
	scanf("%d",&t);
	for (int TT=1;TT<=t;TT++)
	{
		scanf("%d%s",&n,str);
		ans=0;cnt=0;
		for (int i=0;i<=n;i++) if (i<=cnt)
		{
			cnt=cnt+str[i]-'0';
		}
		else
		{
			ans=ans+(i-cnt);
			cnt=i+str[i]-'0';
		}
		printf("Case #%d: %d\n",TT,ans);
	}
	return 0;
}