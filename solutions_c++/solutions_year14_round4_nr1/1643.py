#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;
int S[10005];
int main(void)
{
	int N;
	int X;
	int i;
	int T;
	scanf("%d",&T);
	int tt = 1;
	while(T--)
	{
		scanf("%d %d",&N,&X);
		for(i=0;i<N;i++)
			scanf("%d",&S[i]);
		int lp = 0;
		int rp = N-1;
		sort(S,S+N);
		int ans= 0;
		while(lp<rp)
		{
			if(S[rp]+S[lp]<=X)
			{
				ans++;
				rp--;
				lp++;
			}
			else
			{
				ans++;
				rp--;
			}
		}
		if(lp==rp)
			ans++;
		printf("Case #%d: %d\n",tt++,ans);
	}
}
