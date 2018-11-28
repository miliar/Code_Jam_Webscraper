#include<stdio.h>
#include<algorithm>
#include<vector>
#include<math.h>
#include<string.h>
#include<vector>
#include<map>
#include<set>
#include<iostream>

using namespace std;

typedef long long ll;

int n,m,a[105][105];
char c[1005];
int dir[5][2]={{0,0},{-1,0},{0,-1},{1,0},{0,1}};

bool in(int x,int y)
{
    return x>=0&&x<n&&y>=0&&y<m;
}

void solve()
{
    int r=0;
    int i,j,k;
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            if(a[i][j]==0) continue;
            int cx=i,cy=j,tt=a[i][j];
            while(1)
            {
                cx+=dir[tt][0];cy+=dir[tt][1];
                if(!in(cx,cy)||a[cx][cy]) break;
            }
            if(in(cx,cy)&&a[cx][cy]) continue;
            ++r;
            for(k=1;k<=4;k++)
            {
                cx=i,cy=j;
                tt=k;
                while(1)
                {
                    cx+=dir[tt][0];cy+=dir[tt][1];
                    if(!in(cx,cy)||a[cx][cy]) break;
                }
                if(in(cx,cy)&&a[cx][cy]) break;
            }
            if(k>4) {printf("IMPOSSIBLE\n");return;}
        }
    }
    printf("%d\n",r);
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,I=1,i,j,k;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d %d",&n,&m);
        for(i=0;i<n;i++)
        {
            scanf("%s",c);
            for(j=0;j<m;j++)
            {
                if(c[j]=='.') a[i][j]=0;
                else if(c[j]=='^') a[i][j]=1;
                else if(c[j]=='<') a[i][j]=2;
                else if(c[j]=='v') a[i][j]=3;
                else a[i][j]=4;
            }
        }
        printf("Case #%d: ",I++);
        solve();
    }
    return 0;
}
