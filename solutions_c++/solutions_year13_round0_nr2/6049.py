#include <iostream>
#include<cstdio>
using namespace std;
int a[105][105];
int r[15],c[15];
int main()
{
  freopen("B-small-attempt2.in","r",stdin);
    freopen("output.in","w",stdout);
    int test,i,j,k,n,m;
    scanf("%d",&test);
    for(k=1;k<=test;k++)
    {
        scanf("%d%d",&n,&m);
        for(i=0;i<n;i++)
        r[i]=0;
        for(j=0;j<m;j++)
        c[j]=0;
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                scanf("%d",&a[i][j]);
            }
        }
        int f=0;
        for(i=0;i<n;i++)
        {
            if(a[i][0]==1)
            {
                f=0;
                for(j=0;j<m;j++)
                {
                    if(a[i][j]!=1)
                    {
                        f=1;
                        break;
                    }
                }
                if(f==0)
                r[i]=1;
            }
        }
        for(j=0;j<m;j++)
        {
            if(a[0][j]==1)
            {
                f=0;
                for(i=0;i<n;i++)
                {
                    if(a[i][j]!=1)
                    {
                        f=1;
                        break;
                    }
                }
                if(f==0)
                c[j]=1;
            }
        }
        f=0;
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                if(a[i][j]==1)
                {
                    if(r[i]!=1&&c[j]!=1)
                    {
                        f=1;
                        break;
                    }
                }
            }
            if(f==1)
            break;
        }
        printf("Case #%d: ",k);
        if(f==0)
        printf("YES\n");
        else
        printf("NO\n");
    }
    return 0;
}
