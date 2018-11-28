#include <cstdio>
using namespace std;

int main()
{
	int tt; scanf("%d",&tt);
	for(int t=1;t<=tt;t++)
	{
		int smax;
		char s[1001];
		scanf("%d %s",&smax,s);
		int n = smax+1;
		int standing=0,ans=0;
		for(int a=0;a<n;a++)
		{
			int cur = s[a]-48;
			if(standing < a) { ans += a-standing; standing += (a-standing); }
			standing += cur;
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}