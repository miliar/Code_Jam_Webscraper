#include <stdio.h>
#include <iostream>
#include <math.h>
using namespace std;
int main()
{
    long long int n,t,r,i,y,s;
    s=0;
    scanf("%lld",&n);
    for(i=1; i<=n; i++)
    {
        scanf("%lld",&r);
        scanf("%lld",&t);
        for(s=0; ;s++)
        {
            if((2*r)+1<=t)
            {
                t-=((2*r)+1);s++;r+=2;
            }
            else
                break;
        }
        printf("Case #%lld: %lld\n",i,(s/2));
    }
    return 0;
}


/*
Case #1: 1
Case #2: 2
Case #3: 3
Case #4: 707106780
Case #5: 49
*/