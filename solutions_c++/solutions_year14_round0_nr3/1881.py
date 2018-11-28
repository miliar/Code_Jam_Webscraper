#include <iostream>
#include <cstdio>
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;

#define i64 long long

int R,C,M;
char s[10][10];


int dx[]={-1,-1,-1,0,1,1,1,0};
int dy[]={-1,0,1,1,1,0,-1,-1};

int b[10][10];

int h[6][6];
void DFS(int x,int y)
{
    if(x>=0&&x<R&&y>=0&&y<C&&0==h[x][y])
    {
        h[x][y]=1;
        if(b[x][y]!=0) return;
        int i;
        for(i=0;i<8;i++) DFS(x+dx[i],y+dy[i]);
    }
}



int OK(int x,int y)
{
    int i,j;
    for(i=0;i<R;i++) for(j=0;j<C;j++)
    {
        h[i][j]=0;
    }
    DFS(x,y);

    for(i=0;i<R;i++) for(j=0;j<C;j++)
    {
        if(b[i][j]!=-1)
        {
            if(!h[i][j]) return 0;
        }
    }

    for(i=0;i<R;i++)
    {
        for(j=0;j<C;j++)
        {
            if(b[i][j]==-1) s[i][j]='*';
            else s[i][j]='.';
        }
        s[i][j]=0;
    }
    s[x][y]='c';
    for(i=0;i<R;i++) puts(s[i]);
    return 1;
}

int deal(int a[])
{
    int i,j;





    for(i=0;i<R;i++) for(j=0;j<C;j++)
    {
        b[i][j]=0;
    }
    for(i=0;i<R*C;i++) if(a[i])
    {
        int x=i/C;
        int y=i%C;
        b[x][y]=-1;
        for(j=0;j<8;j++)
        {
            int xx=x+dx[j];
            int yy=y+dy[j];
            if(xx>=0&&xx<R&&yy>=0&&yy<C)
            {
                if(b[xx][yy]!=-1)
                {
                    b[xx][yy]++;
                }
            }
        }
    }
    for(i=0;i<R;i++) for(j=0;j<C;j++)
    {
        if(!b[i][j])
        {
            if(OK(i,j))
            {

                return 1;
            }
        }
    }
    return 0;
}


int DFS(int pos,int re,int a[])
{
    if(0==re)
    {
        return deal(a);
    }
    if(R*C-pos>re&&DFS(pos+1,re,a)) return 1;
    a[pos]=1;
    if(DFS(pos+1,re-1,a)) return 1;
    a[pos]=0;
    return 0;
}

int ok()
{
    if(0==M)
    {
        int i,j;
        for(i=0;i<R;i++)
        {
            for(j=0;j<C;j++)
            {
                s[i][j]='.';
            }
            s[i][j]=0;
        }
        s[0][0]='c';
        for(i=0;i<R;i++) puts(s[i]);
        return 1;
    }
    if(R==1&&C==1&&M==1)
    {
        puts("*");
        return 1;
    }
    if(R*C==M+1)
    {
        int i,j;
        for(i=0;i<R;i++)
        {
            for(j=0;j<C;j++)
            {
                if(i==0&&j==0) putchar('c');
                else putchar('*');
            }
            puts("");
        }
        return 1;
    }
    int a[6*6];
    int i;
    for(i=0;i<R*C;i++) a[i]=0;
    return DFS(0,M,a);
}

int main()
{
    freopen("C-small-attempt3.in","r",stdin);
    freopen("A.out","w",stdout);
    int T;
    scanf("%d",&T);
    int i;
    for(i=1;i<=T;i++)
    {
        scanf("%d%d%d",&R,&C,&M);
        printf("Case #%d:\n",i);
        if(ok())
        {
        }
        else
        {
            puts("Impossible");
        }


    }
}


/*

1
3 5 14

*/

