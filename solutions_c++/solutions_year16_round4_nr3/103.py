#include<bits/stdc++.h>
using namespace std;


int p1[50],p2[50];
int com[50];
int find(int s)
{
    return com[s]==s?s:com[s]=find(com[s]);
}
void uni(int x,int y)
{
    com[find(x)]=find(y);
}
int lx[50][50];
int ly[50][50];
int mat[55][55];
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("2.txt","w",stdout);
    int t,ti=1;scanf("%d",&t);
    while(t--)
    {
        int r,c;
        scanf("%d%d",&r,&c);
        for(int i=0;i<r+c;i++)
            scanf("%d%d",p1+i,p2+i);
        int n=r*c;
        int lim=1<<n;
        int g=r+c+r+c;

        for(int i=0;i<c;i++)
            lx[0][i]=i;
        for(int i=0;i<r;i++)
            ly[i][c]=i+c;
        for(int i=0;i<c;i++)
            lx[r][c-i-1]=i+r+c;
        for(int i=0;i<r;i++)
            ly[r-i-1][0]=i+r+c+c;

        for(int i=1;i<r;i++)
            for(int j=0;j<c;j++)
                lx[i][j]=g++;
        for(int i=1;i<c;i++)
            for(int j=0;j<r;j++)
                ly[j][i]=g++;

        printf("Case #%d:\n",ti++);
        int has=0;
        for(int i=0;i<lim;i++)
        {
            for(int j=0;j<n;j++)
                if((1<<j)&i)mat[j/c][j%c]=1;
                else mat[j/c][j%c]=0;
            for(int j=0;j<g;j++)
                com[j]=j;
            for(int i=0;i<r;i++)
                for(int j=0;j<c;j++)
                    if(mat[i][j]==0)
                    {
                        uni(lx[i][j],ly[i][j]);
                        uni(lx[i+1][j],ly[i][j+1]);
                    }
                    else
                    {
                        uni(lx[i][j],ly[i][j+1]);
                        uni(lx[i+1][j],ly[i][j]);
                    }
            int f=0;
            for(int j=0;j<r+c;j++)
                if(find(p1[j]-1)!=find(p2[j]-1))
                    f=1;
            if(f==0)
            {
                for(int i=0;i<r;i++,puts(""))
                    for(int j=0;j<c;j++)
                        putchar(mat[i][j]?'\\':'/');
                has=1;
                break;
            }
        }
        if(has==0)puts("IMPOSSIBLE");
    }
    return 0;
}
