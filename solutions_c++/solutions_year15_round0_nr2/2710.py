#include<cstdio>
#include<algorithm>

using namespace std;
int D,P[1010];

long long find(int x)
{
	long long ans=0;
	for(int i=1;i<=D;i++)
		if(P[i]>0) ans+=(P[i]-1)/x;
	return ans+x;
}

void work()
{
	scanf("%d",&D);
	for(int i=1;i<=D;i++)
		scanf("%d",&P[i]);
	sort(P+1,P+1+D);
	long long ans=0x3f3f3f3f3f3f3f3fLL;
	for(int i=P[D];i>0;i--)
		ans=min(ans,find(i));
	printf("%lld\n",ans);
}

int main()
{
	freopen("B2.in","r",stdin);
	freopen("B.out","w",stdout);
	int T; scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		work();
	}
}
