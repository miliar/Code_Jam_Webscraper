#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <iostream>
#include <climits>
#include <algorithm>
using namespace std;
#define llt long long int
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    llt t;
    scanf("%lld",&t);
    for(llt k=1;k<=t;k++)
    {
        llt a1,a2,b1[4][4],b2[4][4],temp[17]={0};
        scanf("%lld",&a1);
        for(llt i=0;i<4;i++)
        {
            for(llt j=0;j<4;j++)
                scanf("%lld",&b1[i][j]);//cin>>b1[i][j];
            if(a1==i+1)
            {
                for(llt j=0;j<4;j++)
                    temp[b1[i][j]]=1;
            }
        }
        llt c=0,f=0;
        scanf("%lld",&a2);
        for(llt i=0;i<4;i++)
        {
            for(llt j=0;j<4;j++)
                scanf("%lld",&b2[i][j]);//cin>>b2[i][j];
            if(a2==i+1)
            {
                for(llt j=0;j<4;j++)
                {  if(temp[b2[i][j]])
                   {
                       f++;
                       c=b2[i][j];
                   }
                }
            }
        }
        printf("Case #%lld: ",k);
        if(f==1)
        {
           printf("%lld\n",c);
        }
        else if(f>1)
            printf("Bad magician!\n");
        else
            printf("Volunteer cheated!\n");
    }
    return 0;
}
