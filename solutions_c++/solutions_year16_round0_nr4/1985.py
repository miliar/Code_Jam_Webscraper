#include <bits/stdc++.h>
using namespace std;

int t;

long long k, c, s;

vector <long long> wek;

long long r;
long long d;

int main()
{
    scanf("%d", &t);
    for (int tt=1; tt<=t; tt++)
    {
        scanf("%lld%lld%lld", &k, &c, &s);
        wek.clear();
        r=1;
        d=0;
        for (int i=0; i<k; i++)
        {
            if (i && !(i%c))
            {
                wek.push_back(d+1);
                r=1;
                d=0;
            }
            d+=i*r;
            r*=k;
        }
        wek.push_back(d+1);
        if (wek.size()>s)
        {
            printf("Case #%d: IMPOSSIBLE\n", tt);
        }
        else
        {
            printf("Case #%d:", tt);
            for (int i=0; i<wek.size(); i++)
            {
                printf(" %lld", wek[i]);
            }
            printf("\n");
        }
    }
    return 0;
}
