#include <stdio.h>
#include <memory.h>

using namespace std;

int h[3000];
int N;

void solve()
{
	int i,j,k;
	int tmp[100];
	memset(h,0,sizeof(h));
	for(i=0;i<2*N-1;i++)
	{
		for(j=0;j<N;j++)
		{
			scanf("%d",&tmp[j]);
			//h[tmp]++;
		}
		for(j=0;j<N;j++)
		{
			h[tmp[j]]++;
		}
	}
	
	for(i=0;i<3000;i++)
	{
		if(h[i] % 2 != 0)
			printf(" %d",i);
	}
	printf("\n");
}

int main()
{
	int i, j, k;
	int T, x;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	//freopen("B-small-attempt0.in","r",stdin);
	//freopen("B-small-attempt0.out","w",stdout);
	scanf("%d",&T);
	x=1;
	while(T--)
	{
		scanf("%d",&N);
		printf("Case #%d:",x++);
		solve();
		//printf("%s\n",res);

	}
}