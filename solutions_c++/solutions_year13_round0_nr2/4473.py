#include<iostream>
#include<cstdio>
#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a>b?b:a)

using namespace std;

int n,m,arr[101][101],row[101],col[101];

int myfunc()
{
    int i,j;
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            if(arr[i][j]!=MIN(row[i],col[j]))
            return(0);
        }
    }
    return(1);
}

int main()
{
    FILE *fin=fopen("B-large.in","r");
    FILE *fout=fopen("output1.txt","w");

    int i,j,t,x,ret;
    fscanf(fin,"%d",&t);
    for(x=1;x<=t;x++)
    {
        fscanf(fin,"%d%d",&n,&m);
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            fscanf(fin,"%d",&arr[i][j]);
        }
        for(i=0;i<n;i++)
        {
            row[i]=0;
            for(j=0;j<m;j++)
            row[i]=MAX(row[i],arr[i][j]);
        }
        for(j=0;j<m;j++)
        {
            col[j]=0;
            for(i=0;i<n;i++)
            col[j]=MAX(col[j],arr[i][j]);
        }
        ret=myfunc();
        if(ret==0)
        fprintf(fout,"Case #%d: NO\n",x);
        else
        fprintf(fout,"Case #%d: YES\n",x);
    }
    return(0);
}
