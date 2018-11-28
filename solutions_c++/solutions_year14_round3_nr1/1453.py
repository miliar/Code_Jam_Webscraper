#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <string>
#include <queue>
#include <stack>

#define sqr(x) (x*x)
#define cube(x) (x*x*x)
#define INF 999999999

using namespace std;

long long check_even(long long q)
{
    while(!(q%2))
        q/=2;

    return q;
}

int main()
{
    int t;
    long long p,q;
    char ch;

    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    cin>>t;

    for (int i=1; i<=t; i++)
    {
        scanf("%lld%c%lld",&p,&ch,&q);

        long long g=__gcd(p,q);

        p/=g;
        q/=g;

        printf("Case #%d: ",i);

        if (check_even(q)!=1) cout<<"impossible"<<endl;
        else
        {
            int gen=0;
            if (p>q)
                gen=1;
            while(q>p)
            {
                q/=2;
                gen++;
            }

            cout<<gen<<endl;
        }
    }

    return 0;
}
