#include<cstdio>
#include<cstring>
#define rep(i,n) for(int i=0;i<(n);i++)
using namespace std;
int P[10086],D;
bool check(int time)
{
	rep(split,time)
	{
		int cnt=0;
		rep(i,D)if(P[i]>time-split)
		{
			cnt+=(P[i]/(time-split)-1)+((P[i]%(time-split))!=0);
			if(cnt>split)break;
		}
		if(cnt<=split)return true;
	}
	return false;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,Kase=0;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&D);
		rep(i,D)scanf("%d",&P[i]);
		int L=0,R=1000;
		while(L<R)
		{
			int M=L+R>>1;
			if(check(M))R=M;
			else L=M+1;
		}
		printf("Case #%d: %d\n",++Kase,L);
	}
	return 0;
}

