#include <cstdio>
#include <iostream>
#include <algorithm>
#define MAXN 100
#define MAXM 100
#define SIZE 100
#define MAXC 10000
using namespace std;

struct Cell
{
    int x;
    int y;
    int h;
    Cell()
    {
    }
    Cell(int a,int b,int c)
    {
        x=a;
        y=b;
        h=c;
    }
};

Cell c[MAXC+1];
int a[MAXN+1][MAXM+1],b[MAXN+1][MAXM+1];
int n,m,p;

bool operator<(const Cell &a,const Cell &b)
{
    if(a.h>b.h)
    {
        return true;
    }
    else
    {
        return false;
    }
}

int check()
{
    int i,j,k,l,flag;
    sort(c,c+p);
    for(l=0;l<p;l++)
    {
        i=c[l].x;
        j=c[l].y;
		flag=1;
        for(k=0;(k<m)&&(flag==1);k++)
        {
            if(a[i][k]>a[i][j])
            {
                flag=0;
            }
        }
        for(k=0;(k<m)&&(flag==1);k++)
        {
            b[i][k]=a[i][j];
        }
        flag=1;
        for(k=0;(k<n)&&(flag==1);k++)
        {
            if(a[k][j]>a[i][j])
            {
                flag=0;
            }
        }
        for(k=0;(k<n)&&(flag==1);k++)
        {
            b[k][j]=a[i][j];
        }
    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            if(a[i][j]!=b[i][j])
            {
                return 0;
            }
        }
    }
    return 1;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int i,j,k,t;
    scanf("%d",&t);
    for(k=0;k<t;k++)
    {
        scanf("%d %d",&n,&m);
        p=0;
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                scanf("%d",&a[i][j]);
                b[i][j]=SIZE;
                c[p++]=Cell(i,j,a[i][j]);
            }
        }
        printf("Case #%d: ",k+1);
        if(check()==1)
        {
            printf("YES\n");
        }
        else
        {
            printf("NO\n");
        }
    }
    return 0;
}	
