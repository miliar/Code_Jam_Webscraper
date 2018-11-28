#include<vector>
#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<time.h>
#include<assert.h>
#include<stdlib.h>
using namespace std;
int a[105][105];
int main()
{
    int t,n,m;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        scanf("%d %d",&n,&m);
        for(int j=0;j<n;j++)
        {
            for(int k=0;k<m;k++)
            {
                 scanf("%d",&a[j][k]);
            }
        }
        bool chk=1;
         for(int j=0;j<n;j++)
        {
            for(int k=0;k<m;k++)
            {
                bool chk1=0,chk2=0;
                 for(int ii=0;ii<n;ii++)
                 {
                     if(a[ii][k]>a[j][k])
                     {
                         chk1=1;
                         break;
                     }
                 }

                  for(int ii=0;ii<m;ii++)
                 {
                     if(a[j][ii]>a[j][k])
                     {
                         chk2=1;
                         break;
                     }
                 }

                 if(chk1&&chk2)
                 {chk=0;break;}
            }
        }
        if(chk)
        printf("Case #%d: YES\n",i);
        else
           printf("Case #%d: NO\n",i);
    }
    return 0;
}
