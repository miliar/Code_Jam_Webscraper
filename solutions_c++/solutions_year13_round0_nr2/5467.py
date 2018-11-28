#include<iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include<math.h>
using namespace std;

    int main()
{
    int T;
    cin>>T;
    for (int z=1;z<=T;z++)
    {
        int n,m;
        cin>>n>>m;
        int a[n][m];
        for (int i=0;i<n;i++)
       for (int j=0;j<m;j++)
       cin>>a[i][j];

int w=1;
       for (int i=0;i<n;i++)
       {
       for (int j=0;j<m;j++)
       {
           int fail=0,win=0,found=0;
           if (a[i][j]==1)
           {
               found=1;

               for (int l=0;l<m;l++)
               {
                   if (a[i][l]==2)
                   {fail=1;break;}
               }
               if (fail==0){win=1;}
               fail=0;
               if (win==0)
               {
               for (int l=0;l<n;l++)
               {
                   if (a[l][j]==2)
                   {fail=1;break;}
               }
               if (fail==0){win=1;}
               }
          }

          if (win==0&&found==1){w=0;break;}
       }
       if(w==0)
       break;
       }

       cout<<"Case #"<<z<<": ";
       if (w==1){cout<<"YES\n";}
       else if (w==0){cout<<"NO\n";}

    }
}
