#include <iostream>
#include <stdio.h>
using namespace std;
typedef double Double;
#define MAX 100000

Double DP[MAX+1];
Double C,F,X;
int t;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output2.txt","w",stdout);

    int test,i,j;
    Double CPS;
    Double MinTime;
    Double CurTime;

    scanf("%d",&t);

    for (test=1;test<=t;test++)
    {
        cin>>C>>F>>X;

        DP[0]=0.0;
        MinTime=X/2.0;

        for (i=1;i<=MAX;i++)
        {
            CPS=2.0+(Double)(i-1)*F;
            DP[i]=DP[i-1]+C/CPS;

            CPS=2.0+(Double)(i)*F;
            CurTime=X/CPS+DP[i];

            if (CurTime<MinTime)
            MinTime=CurTime;
        }

        printf("Case #%d: %.7f\n",test,(double)MinTime);
    }

    return 0;
}
