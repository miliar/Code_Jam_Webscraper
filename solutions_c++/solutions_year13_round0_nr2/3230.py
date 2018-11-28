#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string.h>
#include<limits.h>
#include<map>
#include<queue>
#include<vector>
using namespace std;
int ar[200][200],n,m;
bool checkrow(int i,int x)
{
     for(int j=0;j<m;j++)
     {
             if(ar[i][j]>x)
             return 0;
     }
     return 1;
}
bool checkcol(int j,int x)
{
     for(int i=0;i<n;i++)
     {
             if(ar[i][j]>x)
             return 0;
     }
     return 1;
}
int main()
{
     int t,flag,cases=0;
    freopen("B-large.in","r",stdin);
     freopen("g.txt","w",stdout);
     scanf("%d",&t);
     while(t--)
     {
               cases++;
               printf("Case #%d: ",cases);
               scanf("%d%d",&n,&m);
               for(int i=0;i<n;i++)
               for(int j=0;j<m;j++)
               scanf("%d",&ar[i][j]);
               flag=0;
               for(int i=0;i<n;i++)
               {
                       for(int j=0;j<m;j++)
                       {

                                              if(!(checkrow(i,ar[i][j])||checkcol(j,ar[i][j])))
                                              {flag=1;break;}
                       }
               }
               if(flag==0)
               printf("YES\n");
               else
               printf("NO\n");
                                              
     
     }
}
