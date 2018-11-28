#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<cstring>
#include<string>
#include<algorithm>

using namespace std;

int a[200][200],rm[200],cm[200];
bool r[200],c[200];

int main()
{
    freopen("x.in","r",stdin);
    freopen("x.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int K=1;K<=T;K++)
    {
        int n,m;
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)
          for(int j=0;j<m;j++)
            scanf("%d",&a[i][j]);
        memset(r,true,sizeof(r));
        memset(c,true,sizeof(c));
        for(int i=0;i<n;i++)
        {
           rm[i]=a[i][0];
           for(int j=1;j<m;j++)
             rm[i]=max(rm[i],a[i][j]);
        }
        for(int j=0;j<m;j++)
        {
           cm[j]=a[0][j];
           for(int i=1;i<n;i++)
             cm[j]=max(cm[j],a[i][j]);
        }
        bool flag=true;
        for(int k=1;k<=100;k++)
        {
            for(int i=0;i<n;i++)
            if(r[i])
            {
              for(int j=0;j<m;j++)
                if(c[j] && a[i][j]==k)
                {
                    if(rm[i]>k && cm[j]>k){flag=false;break;}
                    if(rm[i]<=k)r[i]=false;
                    if(cm[j]<=k)c[j]=false;
                }
              if(!flag)break;
            }
            if(!flag)break;
        }
        printf("Case #%d: ",K);
        if(flag)puts("YES");
        else    puts("NO");
    }
    return 0;
}
