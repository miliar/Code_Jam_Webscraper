#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<queue>
#include<stack>
#include<vector>
#include<map>
#include<set>
#include<string>
#include<deque>
#pragma comment(linker, "/STACK:1024000000,1024000000")
using namespace std;
#define INF 0x3f3f3f3f
#define eps 1e-8
#define maxn 11005
#define mod 1000000007
#define FI first
#define SE second
char s[105][105];
int n,m;
int dx[4]={1,-1,0,0};
int dy[4]={0,0,1,-1};
int out[105][105];
int in[105][105];
int c[105];
int r[105];
int all=0;
bool ok(int x,int y)
{
    if(x>=0&&x<n&&y>=0&&y<m)    return 1;
    return 0;
}
void f(int x,int y,int k)
{
    int tx = x, ty = y;
    do{
            tx += dx[k] ; ty += dy[k] ;
            if (!ok(tx,ty)) break ;
            if (s[tx][ty] != '.')
            {
                out[x][y]++;
                in[tx][ty]++;
                break ;
            }
        }while (true) ;
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {
        scanf("%d%d",&n,&m);
        memset(in,0,sizeof(in));
        memset(out,0,sizeof(out));
        memset(c,0,sizeof(c));
        memset(r,0,sizeof(r));
        for(int i=0;i<n;i++)    scanf("%s",s[i]);
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(s[i][j]=='.') continue;
                r[i]++;c[j]++;
                if(s[i][j]=='^')    f(i,j,1);
                if(s[i][j]=='v')    f(i,j,0);
                if(s[i][j]=='<')     f(i,j,3);
                if(s[i][j]=='>')    f(i,j,2);
            }
        }
        int sign=0;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(s[i][j]=='.')    continue;
                if(r[i]==1&&c[j]==1)
                {
                    sign=1;
                    break;
                }
                if(out[i][j]==0)
                {
                    all++;
                }
            }
            if(sign==1) break;
        }
        printf("Case #%d: ",cas);
        if(sign==1) printf("IMPOSSIBLE\n");
        else printf("%d\n",all);
        all=0;
    }
}
