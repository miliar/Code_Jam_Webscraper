//BISMILLAHIR RAHMANIR RAHIM
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<string>
#include<map>
#include<queue>
#include<vector>
#include<iostream>
using namespace std;
#define inf 1<<25
#define sz 2000
int main()
{
    freopen("magitian.txt","w",stdout);
    int ar[10][10],br[10][10],i,t,q1,q2,p,rr[10],k,m,j;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        scanf("%d",&q1);
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                scanf("%d",&ar[i][j]);
                if(i==q1)
                    rr[j]=ar[i][j];
            }
        }

        scanf("%d",&q2);
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                scanf("%d",&br[i][j]);
            }
        }
        p=0;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                if(br[q2][i]==rr[j])
                {
                      p++;
                      m=rr[j];
                }

            }
        }
        if(p==0)
            printf("Case #%d: Volunteer cheated!\n",k);
        else if(p==1)
            printf("Case #%d: %d\n",k,m);
        else if(p>1)
            printf("Case #%d: Bad magician!\n",k);
    }
    return 0;
}


