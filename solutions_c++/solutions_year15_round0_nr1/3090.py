#include <cstdio>
#include <cstdlib>
using namespace std;

int T,n,cnt,Ans;
char s[100001];

int main()
{
	
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	scanf("%d",&T);
	for (int Case=1;Case<=T;Case++)
	{
		scanf("%d",&n);
		scanf("%s",s); cnt=0; Ans=0;
		for (int i=0;i<=n;i++)
		{
			if (cnt<i)
			{
				Ans+=i-cnt; cnt=i;
			}
			cnt+=s[i]-'0';
		}
		printf("Case #%d: %d\n",Case,Ans);
	}
}

