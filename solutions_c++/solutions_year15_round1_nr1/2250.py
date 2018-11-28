#include<cstdio>
#include<algorithm>
using namespace std;

int N,mush[1010];

int way1()
{
	int ans=0;
	for(int i=1;i<N;i++)
		ans+=max(mush[i]-mush[i+1],0);
	return ans;
}
int way2()
{
	int eat=0;
	for(int i=2;i<=N;i++)
		eat=max(mush[i-1]-mush[i],eat);
	//printf("\neat %d\n",eat);
	int ans=0;
	for(int i=1;i<N;i++) ans+=min(mush[i],eat);
	return ans;
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int T; scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		scanf("%d",&N);
		for(int j=1;j<=N;j++) 
			scanf("%d",&mush[j]);
		printf("Case #%d: %d %d\n",i,way1(),way2());
	}
	return 0;
}
