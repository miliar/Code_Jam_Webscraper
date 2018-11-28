#include <cstdio>
#include <cstdlib>
#include <set>
using namespace std;

int T,n;
int a[1001],ans;
int f[1001][1001];

int calc(int x,int y)
{
	return (x-1)/y;
}

int main()
{
	
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
//	printf("%d\n",calc(9,4));
	
	scanf("%d",&T);
	for (int Case=1;Case<=T;Case++)
	{
		scanf("%d",&n); ans=0;
		for (int i=1;i<=n;i++) scanf("%d",&a[i]),ans=max(ans,a[i]);;
		for (int lim=1;lim<=1000;lim++)
		{
			int cnt=0;
			for (int i=1;i<=n;i++) cnt+=calc(a[i],lim);
			if (cnt+lim<ans) ans=cnt+lim;
		}
		printf("Case #%d: %d\n",Case,ans);
	}
}

