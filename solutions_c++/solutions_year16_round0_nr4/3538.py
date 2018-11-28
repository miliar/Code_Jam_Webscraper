#include <stdio.h>
#include <string.h>
int T,t,K,C,S;
char temp[1100];


void solve()
{
	int i,j,k;
	int d;
	int res = 0;
	

	for(i=1;i<S;i++)
		printf("%d ",i);
	printf("%d\n",S);
}


int main()
{
	int i,j,k,x;
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%d %d %d",&K,&C,&S);
		printf("Case #%d: ",t);
		solve();
		//printf("Case #%d: %d\n",t,solve());
		//printf("%d %s\n",S,temp);
		//printf("Case #%d: %d\n",i,solve());

	}

	//gets(temp);
	return 0;
}
