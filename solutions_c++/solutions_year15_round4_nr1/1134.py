#include<bits/stdc++.h>
using namespace std;

char a[105][105];
int n,m;

inline bool chk(int x,int y,int tx,int ty)
{
	for(;;)
	{
		x+=tx;y+=ty;
		if(x>=n||x<0||y>=m||y<0)
			return 1;
		if(a[x][y]!='.')
			return 0;
	}
	return 1;
}

int main()
{freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
	int T,t,i,j,s;
	for(scanf("%d",&T),t=1;t<=T;t++)
	{
		for(scanf("%d%d",&n,&m),i=0;i<n;i++)
			scanf("%s",a[i]);
		printf("Case #%d: ",t);
		for(s=i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
				if(a[i][j]!='.')
				{
					switch(a[i][j])
					{
					case '^':if(chk(i,j,-1,0))s++;break;
					case '>':if(chk(i,j,0,1))s++;break;
					case '<':if(chk(i,j,0,-1))s++;break;
					case 'v':if(chk(i,j,1,0))s++;break;
					}
					if(chk(i,j,-1,0)&&chk(i,j,1,0)&&chk(i,j,0,-1)&&chk(i,j,0,1))
						break;
				}
			if(j<m)
				break;
		}
		if(i<n)
			puts("IMPOSSIBLE");
		else
			printf("%d\n",s);
	}
	return 0;
}
