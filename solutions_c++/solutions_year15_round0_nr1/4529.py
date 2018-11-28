#include <cstdio>
#define MAXS 1010
using namespace std;

// String
char str[MAXS];

// Main
int main(void)
{
	int tc, cs, now, i, n, ans;

	// Read Input
	scanf("%d",&tc);
	for(cs=1;cs<=tc;cs++)
	{
		scanf("%d",&n);
		scanf("%s",str);

		// Greedy
		now=ans=0;
		for(i=0;i<=n;i++)
		{
			if(str[i]=='0') continue;
			if(now<i)
			{
				ans+=(i-now);
				now+=(i-now);
			}
			now+=(str[i]-'0');
		}
		printf("Case #%d: %d\n",cs,ans);
	}
	return 0;
}