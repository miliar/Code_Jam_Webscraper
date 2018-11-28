#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;
typedef long double Double;

int t;
int n,k;
Double P[211];

int mypopctr(int mask)
{
    int ctr=0;

    while(mask>0)
    {
        if (mask%2==1)
        ctr++;

        mask/=2;
    }

    return ctr;
}


int L=0;
Double Prob[211];

Double Help[211];
Double Yes[211];

Double GetVal()
{
    int i,j;

    for (i=1;i<=L;i++)
    {
        Yes[i]=0.0;
    }
    Yes[0]=1.0;

    for (i=1;i<=L;i++)
    {
        Help[0]=Yes[0]*(1.0-Prob[i]);

        for (j=0;j<=i;j++)
        {
            Help[j]=Yes[j]*(1.0-Prob[i]) + Yes[j-1]*Prob[i];
        }

        for (j=0;j<=i;j++)
        {
            Yes[j]=Help[j];
        }
    }

    return Yes[L/2];
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int test;
    int i,j;
    int mask;
    Double val,bestval=0.0;

    scanf("%d",&t);

    for (test=1;test<=t;test++)
    {
        bestval=0.0;

        scanf("%d %d",&n,&k);

        for (i=1;i<=n;i++)
        {
            cin>>P[i];
        }

        sort(P+1,P+1+n);

        for (i=0;i<=k;i++)
        {
            L=0;

            for (j=1;j<=i;j++)
            {
                L++;
                Prob[L]=P[j];
            }

            for (j=n;j>=1;j--)
            {
                if (L==k)
                break;

                L++;
                Prob[L]=P[j];
            }

            val=GetVal();

            if (val>bestval)
            bestval=val;
        }

        printf("Case #%d: %.8f\n",test,(double)bestval);
    }

    return 0;
}
