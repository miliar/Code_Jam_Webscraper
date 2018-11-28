#include<iostream>
#include<stdio.h>
using namespace std;
int a[105][105];
bool b[105][105];
int c[105];
int main()
{
    int t,i,j,k,count,n,m,r;
    scanf("%d",&t);
    for(count=1;count<=t;++count)
    {
        scanf("%d%d",&n,&m);
        for(i=0;i<n;++i)
            for(j=0;j<m;++j)
            { scanf("%d",&a[i][j]); b[i][j]=false; }
        for(i=0;i<n;++i)
        {
            for(j=0;j<m;++j)
            {
                if(!b[i][j])
                {
                    for(k=0;k<n;++k)
                    {
                        if(a[k][j]>a[i][j]) break;
                    }
                    if(k==n) 
                    {
                        b[i][j]=true;
                        for(k=0;k<n;++k)
                        {
                            if(a[k][j]==a[i][j]) b[k][j]=true;
                        }
                    }
                    else
                    {
                        for(r=0;r<m;++r)
                        {
                            if(a[i][r]>a[i][j]) break;
                        }
                        if(r==m)
                        {
                            b[i][j]=true;
                            for(r=0;r<m;++r)
                            {
                                if(a[i][r]==a[i][j]) b[i][r]=true;
                            }
                        }
                        else
                        {
                            //printf("Case #%d: No\n",count);
                            c[count-1]=0;
                            break;
                        }
                    }
                }
            }
            if(j!=m) break;
        }
        if(i==n)
        {
            //printf("Case #%d: Yes\n",count); 
            c[count-1]=1;
        }
    }
    for(i=0;i<t;++i)
    {
        if(c[i]==0)
          printf("Case #%d: NO\n",i+1);
        else
          printf("Case #%d: YES\n",i+1);
    }
    getchar(); getchar();
    return 0;
}
