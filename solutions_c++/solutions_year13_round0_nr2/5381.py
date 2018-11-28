#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<string>
#include<cstring>

using namespace std;
int a[11][11],b[11][11];
int main()
{
    int i,j,flag,t,k,p,n,m,cnt;
    scanf("%d",&t);
    k=1;
    while(k<=t)
    {
         cin>>n>>m;
         for(i=0;i<n;i++)
         for(j=0;j<m;j++)
         {cin>>a[i][j];b[i][j]=0;}
         flag=0;
         for(i=0;i<n;i++)
         {
              for(j=0;j<m;j++)
              {
                    if(a[i][j]==1)
                    {
                        cnt=0;
                        for(p=0;p<m;p++)
                        if(a[i][p]==1)
                        cnt++;
                        if(cnt==m)
                        b[i][j]=1;
                        cnt=0;
                        for(p=0;p<n;p++)
                        if(a[p][j]==1)
                        cnt++;
                        if(cnt==n)
                        b[i][j]=1;
                        cnt=0;
                    }
                    else if(a[i][j]==2)
                    b[i][j]=1;
              }
         }
         for(i=0;i<n;i++)
         for(j=0;j<m;j++)
         if(b[i][j]==0)
         {flag=1;i=n;break;}
         
         if(flag==1)
         printf("Case #%d: NO\n",k);
         else if(flag==0)
         printf("Case #%d: YES\n",k);
         k++;
    }
    return 0;
}
