#include<iostream>
#include<vector>
#include<string.h>
#include<set>
#include<algorithm>
#include<math.h>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

#define s(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
typedef long long int ll;
int ar[100][100],n,m;
int mark[105];
bool allrow()
{
    bool ok;
    int i,j;
    for(i=0;i<n;i++)
    {
        for(j=1;j<m;j++)
        {
            if(ar[i][j]!=ar[i][0])
            return false;
        }
    }
    return true;

}
bool allcol()
{
    bool ok;
    int i,j;
    for(i=0;i<m;i++)
    {
        for(j=1;j<n;j++)
        {
            if(ar[j][i]!=ar[0][i])
            return false;
        }
    }
    return true;

}
int main()
{
   int t,i,j,test,k,r;
   //ios::sync_with_stdio(false);
   freopen("B.in","r",stdin);
   freopen("B.out","w",stdout);
   cin>>t;
   for(test=1;test<=t;test++)
   {
       for(i=0;i<105;i++)
       mark[i]=0;
       cin>>n>>m;
       int ar2[n][m];
       int a[n][m];
       rep(i,n)
       {
           rep(j,m)
            {cin>>ar[i][j];
            a[i][j]=ar[i][j];}
       }
       if(n==1 || m==1)
       {
           printf("Case #%d: YES\n",test);
           continue;
       }
       if(allrow() || allcol())
       {
            printf("Case #%d: YES\n",test);
           continue;
       }
       for(i=0;i<n;i++)
       {
           for(j=0;j<m;j++)
           {
               mark[ar[i][j]]=1;
           }
       }
       for(r=100;r>=1;r--){

           if(mark[r]==1){
               for(i=0;i<n;i++)
               {
                   for(j=0;j<m;j++)
                   {
                       if(ar[i][j]==r)
                       {
                           //cout<<i<<" "<<j<<" "<<r<<endl;
                           bool row1=true,col1=true;
                           for(k=0;k<m;k++)
                           {
                               if(a[i][k]==-1)
                               {
                                   row1=false;
                                   break;
                               }
                           }
                           for(k=0;k<n;k++)
                           {
                               if(a[k][j]==-1)
                               {
                                   col1=false;
                                   break;
                               }
                           }
                           if(row1)
                           {
                               for(k=0;k<m;k++)
                               ar2[i][k]=r;
                           }
                           if(col1)
                           {
                               for(k=0;k<n;k++)
                               ar2[k][j]=r;
                           }
                           a[i][j]=-1;
                       }

                   }
               }

       }
       }

       /*cout<<"\n \n";
       for(i=0;i<n;i++)
       {
           for(j=0;j<m;j++)
           {
               cout<<ar2[i][j]<<" ";

           }
           cout<<endl;
       }*/
       bool ok=true;
       for(i=0;i<n;i++)
       {
           for(j=0;j<m;j++)
           {
               if(ar[i][j]!=ar2[i][j])
               {
                   ok=false;
                   break;
               }
           }
           if(!ok)
           break;
       }
       if(ok)
       printf("Case #%d: YES\n",test);
       else
       printf("Case #%d: NO\n",test);
   }
   return 0;
}
