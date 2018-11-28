#include<cstdio>
#include<cstring>
#include<cmath>
#include<iomanip>
using namespace std;
int n;
int a[1010],b[1010];
int solve(int lim)
{
	memcpy(a,b,sizeof(a));
	int ans=0,M=0;
	for (int i=1;i<=n;i++)
	{
		if (a[i]%lim==0)
		{
			ans+=a[i]/lim-1;
			a[i]=lim;
		}
		else 
		{
			ans+=a[i]/lim;
			a[i]%=lim;
		}
		M=max(M,a[i]);
	}
	if (ans) M=lim;
	return ans+M;
}
void work(int lab)
{
	printf("Case #%d: ",lab);
	scanf("%d",&n);
	int r=0;
	for (int i=1;i<=n;i++)
	scanf("%d",&a[i]),r=max(r,a[i]);
	memcpy(b,a,sizeof(b));
	int ans=r;
	for (int i=1;i<=r;i++)
	ans=min(ans,solve(i));
	printf("%d\n",ans);
}
int main()
{
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
	int t;
	scanf("%d",&t);
	for (int i=1;i<=t;i++)work(i);
	return 0;
}
