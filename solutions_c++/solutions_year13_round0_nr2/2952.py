#include<cstdio>

#define N 100
#define M 100

int tab[N][M];
int t,n,m;

bool test()
{
	int i,j,k,l;
	bool ret=true;
	for(i=0;i<n;i++)
		for(j=0;j<m;j++)
		{
			for(k=0;k<m;k++)if(tab[i][k]>tab[i][j])break;
			for(l=0;l<n;l++)if(tab[l][j]>tab[i][j])break;
			//printf("i:%d j:%d k:%d l:%d m:%d n:%d\n",i,j,k,l,m,n);
			if(k!=m&&l!=n)return ret=false;
		}
	return ret;
}

int main()
{
	scanf("%d",&t);
	int cas;
	for(cas=1;cas<=t;cas++)
	{
		scanf("%d%d",&n,&m);
		int i,j;
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)scanf("%d",tab[i]+j);
		printf("Case #%d: ",cas);
		bool ret=test();
		if(ret)printf("YES\n");
		else printf("NO\n");	
	}
	return 0;
}
