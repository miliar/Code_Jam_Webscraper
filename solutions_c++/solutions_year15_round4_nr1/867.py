#include<iostream>
#include<cstdio>
#include<algorithm>
#include<fstream>
#include<vector>
#include<queue>
using namespace std;
long long t,n,m,used[101][101],lr[101][101],ur[101][101],lc[101][101],uc[101][101];
char s[101][101];
int func(int x, int y)
{
    if(used[x][y]==1) return 0;
    used[x][y]=1;
    if(s[x][y]=='^')
    {
        if(lr[x][y]==0) return 1;
        else return func(lr[x][y],y);
    }
    if(s[x][y]=='v')
    {
        if(ur[x][y]==0) return 1;
        else return func(ur[x][y],y);
    }
    if(s[x][y]=='<')
    {
        if(lc[x][y]==0) return 1;
        else return func(x,lc[x][y]);
    }
    if(s[x][y]=='>')
    {
        if(uc[x][y]==0) return 1;
        else return func(x,uc[x][y]);
    }
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%lld",&t);
	for(int o=1; o<=t; o++)
	{
		scanf("%lld%lld",&n,&m);
		for(int i=1; i<=n; i++)
        {
            scanf("\n");
            for(int j=1; j<=m; j++)
            {
                scanf("%c",&s[i][j]);
            }
        }
        for(int i=1; i<=n; i++)
        {
            for(int j=1; j<=m; j++)
            {
                used[i][j]=lr[i][j]=ur[i][j]=lc[i][j]=uc[i][j]=0;
            }
        }
        for(int i=1; i<=n; i++)
        {
            for(int j=1; j<=m; j++)
            {
                for(int l=i-1; l>=1; l--)
                {
                    if(s[l][j]!='.') {lr[i][j]=l; break;}
                }
                for(int l=i+1; l<=n; l++)
                {
                    if(s[l][j]!='.') {ur[i][j]=l; break;}
                }
                for(int l=j-1; l>=1; l--)
                {
                    if(s[i][l]!='.') {lc[i][j]=l; break;}
                }
                for(int l=j+1; l<=m; l++)
                {
                    if(s[i][l]!='.') {uc[i][j]=l; break;}
                }
            }
        }
        int e=0,ans=0;
        for(int i=1; i<=n; i++)
        {
            if(e==1) break;
            for(int j=1; j<=m; j++)
            {
                if(e==1) break;
                if(s[i][j]=='.') continue;
                else if(used[i][j]==1) continue;
                if(lr[i][j]==0&&ur[i][j]==0&&lc[i][j]==0&&uc[i][j]==0)
                {
                    printf("Case #%d: IMPOSSIBLE\n",o); e=1; break;
                }
                //cout<<lr[i][j]<<" "<<ur[i][j]<<" "<<lc[i][j]<<" "<<uc[i][j]<<endl;
                if((s[i][j]=='^'&&lr[i][j]==0)||(s[i][j]=='v'&&ur[i][j]==0)||(s[i][j]=='<'&&lc[i][j]==0)||(s[i][j]=='>'&&uc[i][j]==0))
                {
                    if(lr[i][j]!=0) s[i][j]='^';
                    else if(ur[i][j]!=0) s[i][j]='v';
                    else if(lc[i][j]!=0) s[i][j]='<';
                    else if(uc[i][j]!=0) s[i][j]='>';
                    ans++;
                    used[i][j]==1;
                }
                ans+=func(i,j);
            }
        }
        if(e==1) continue;
        printf("Case #%d: %d\n",o,ans);
	}
	return 0;
}
