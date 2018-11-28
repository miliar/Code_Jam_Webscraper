#include <stdio.h>
int tcase,n,m,ans;
char str[110][110];
int main()
{
	int i,j,k,l,loop;
	int xx[5]={0,-1,0,1,0};
	int yy[5]={0,0,1,0,-1};
	bool flag=false;
	char temp;

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	scanf("%d",&tcase);
	for(loop=1;loop<=tcase;loop++)
	{
		scanf("%d %d",&n,&m);
		for(i=1;i<=n;i++)
		{
			scanf("%s",str[i]+1);
			for(j=1;j<=m;j++)
			{
				if(str[i][j]=='^') str[i][j]=1;
				if(str[i][j]=='>') str[i][j]=2;
				if(str[i][j]=='v') str[i][j]=3;
				if(str[i][j]=='<') str[i][j]=4;
			}
		}
		ans=0;
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=m;j++)
			{
				if(str[i][j]!='.')
				{
					flag=false;
					temp=str[i][j];
					for(k=1;;k++)
					{
						if(i+k*xx[temp]<1 || i+k*xx[temp]>n || j+k*yy[temp]<1 || j+k*yy[temp]>m)
						{
							flag=true;
							break;
						}
						if(str[i+k*xx[temp]][j+k*yy[temp]]!='.')
							break;
					}
					if(flag==true)
					{
						for(l=1;l<=4;l++)
						{
							flag=false;
							for(k=1;;k++)
							{
								if(i+k*xx[l]<1 || i+k*xx[l]>n || j+k*yy[l]<1 || j+k*yy[l]>m)
								{
									flag=true;
									break;
								}
								if(str[i+k*xx[l]][j+k*yy[l]]!='.')
									break;
							}
							if(flag==false) break;
						}
						if(l==5)
						{
							ans=-1;
							goto end;
							break;
						}
						else
							ans++;
					}
				}
			}
		}
	end:
		if(ans==-1)
			printf("Case #%d: IMPOSSIBLE\n",loop);
		else
			printf("Case #%d: %d\n",loop,ans);
	}
	return 0;
}