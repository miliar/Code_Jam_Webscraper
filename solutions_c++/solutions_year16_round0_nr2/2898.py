#include <cstdio>
#include <cstring>
#include <algorithm>
#define fo(i,a,b) for (int i = a;i <= b;i ++)

using namespace std;

int T,cas,len;
char s[105];

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	for (scanf("%d",&T);T;T --)
	{
		printf("Case #%d: ",++cas);
		scanf("%s",s+1);
		len = strlen(s+1);
		int ans = 0;
		fo(i,1,len-1)
			if (s[i] != s[i+1]) ans ++;
		if (s[len] == '-') ans ++;
		printf("%d\n",ans);
	}
	return 0;
}
