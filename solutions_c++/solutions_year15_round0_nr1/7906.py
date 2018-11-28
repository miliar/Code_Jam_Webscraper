#include <cstdio>
#include <cstdlib>
#define N 1005
using namespace std;

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int cnt_case,n;
	scanf("%d",&cnt_case);
	for(int ii=1;ii<=cnt_case;++ii)
	{
		static char s[N];
		scanf("%d%s",&n,s);
		int cnt=0,ans=0;
		for(int i=0;i<=n;++i)
		{
			if(cnt<i) ans+=i-cnt,cnt=i;
			cnt+=s[i]-'0';
		}
		printf("Case #%d: %d\n",ii,ans);
	}
	return 0;
}

