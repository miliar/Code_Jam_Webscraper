#include<cstdio>

char s[111][111];

int px[4]={-1,1,0,0};
int py[4]={0,0,1,-1};

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
    int tc,tcn;
    scanf("%d",&tcn);
    for(tc=1;tc<=tcn;tc++)
	{
		int x,y,r=0;
		int i,j,k,n,m;
		scanf("%d%d",&n,&m);
        for(i=1;i<=n;i++)scanf("%s",s[i]+1);
        for(i=1;i<=n;i++)for(j=1;j<=m;j++)if(s[i][j]!='.')
		{
			if(s[i][j]=='^')k=0;
			if(s[i][j]=='v')k=1;
			if(s[i][j]=='>')k=2;
			if(s[i][j]=='<')k=3;
            x=i;y=j;
            while(x>=1&&x<=n&&y>=1&&y<=m)
			{
                x+=px[k];
                y+=py[k];
                if(x>=1&&x<=n&&y>=1&&y<=m&&s[x][y]!='.')break;
			}
            if(x>=1&&x<=n&&y>=1&&y<=m)continue;
            for(k=0;k<4;k++)
			{
				x=i;y=j;
				while(x>=1&&x<=n&&y>=1&&y<=m)
				{
					x+=px[k];
					y+=py[k];
					if(x>=1&&x<=n&&y>=1&&y<=m&&s[x][y]!='.')break;
				}
				if(x>=1&&x<=n&&y>=1&&y<=m)break;
			}
			if(k==4)r=-1e9;
			r++;
		}
		if(r<0)printf("Case #%d: IMPOSSIBLE\n",tc);
		else printf("Case #%d: %d\n",tc,r);
	}
}
