#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

int main()
{
    freopen("cookie.in","r",stdin);
    freopen("cookie.out","w",stdout);
    int test;
    scanf("%d",&test);
    double c,f,x;
    int cases=0;
    while(test)
    {
        cases++;
        scanf("%lf%lf%lf",&c,&f,&x);
        double counter=0.0;
        double ans;
        double k=2.0;

        while(1)
        {
            ans=x/k;
            if(ans < ((c/k)+(x/(k+f))) )
            {
                counter=counter+ans;
                break;
            }
            else
            {
                counter=counter+(c/k);
            }
            k=k+f;
        }

        printf("Case #%d: %.7lf",cases,counter);

        test--;
        if(test>0) printf("\n");
    }

    return 0;
}
