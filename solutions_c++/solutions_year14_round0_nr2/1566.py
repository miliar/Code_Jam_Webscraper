#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#define ll long long
#define eps 1e-9
using namespace std;

int ar[5][5];
int br[20];

int main()
{
    freopen("0.in","r",stdin);
    freopen("0.out","w",stdout);

    int a,b,c,d,e,t;
    double x,y,z,C,F,Z,X;

    cin>>t;

    for(int i=1;i<=t;i++)
    {
        cin>>C>>F>>X;
        C=C+eps;
        F=F+eps;
        X=X+eps;

        z=(X/2);

        if(X<=C)
        {
            printf("Case #%d: %.7lf\n",i,z);
            continue;
        }

        Z=0.00;
        x=0.00;
        double rate;
        rate=2;

        for(a=0;a<=2000000;a++)
        {
            Z=Z+(C/rate);
            rate=rate+F;
            y=X/rate;
            z=min(z,Z+y);
        }
        printf("Case #%d: %.7lf\n",i,z);
    }


    return 0;
}
