#include<stdio.h>
int in[105][105];
int n,m;
bool chr(int x)
{
	int a;
	for(a=0;a<m;a++)
		if(in[x][a]==2)
			return 0;
	return 1;
}
bool chc(int x)
{
	int a;
	for(a=0;a<n;a++)
		if(in[a][x]==2)
			return 0;
	return 1;
}
int main()
{
	//freopen("B-small-attempt0.in","r",stdin);
	//freopen("B-small-attempt0.txt","w",stdout);
	int a,b,c,t;
	bool ck;
	scanf("%d",&t);
	for(a=0;a<t;a++)
	{
		scanf("%d%d",&n,&m);
		for(b=0;b<n;b++)
			for(c=0;c<m;c++)
				scanf("%d",&in[b][c]);
		printf("Case #%d: ",a+1);
		for(b=0,ck=0;b<n;b++)
		{
			for(c=0;c<m;c++)
				if(in[b][c]==1)
					if(!chr(b) && !chc(c))
					{
						printf("NO\n");
						ck=1;
						break;
					}
			if(ck)	break;
		}
		if(!ck)
			printf("YES\n");
	}
}
