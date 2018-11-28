#include <iostream>
#include <stdio.h>
using namespace std;

double nujnovreme[100001];
double C,F,X;
int t;
double minvreme;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output_large.txt","w",stdout);

    int i,j;

    cin>>t;

    for (i=1;i<=t;i++)
    {
        cin>>C>>F>>X;

        nujnovreme[0]=0.0;

        minvreme=X/2.0;

        for (j=1;j<=100000;j++)
        {
            nujnovreme[j]=nujnovreme[j-1]+C/(2.0+(double)(j-1)*F);

            if ( minvreme>nujnovreme[j]+X/(2.0+(double)j*F) ) minvreme=nujnovreme[j]+X/(2.0+(double)j*F);
        }

        cout<<"Case #"<<i<<": ";
        printf("%.7f\n",minvreme);
    }

    return 0;
}
