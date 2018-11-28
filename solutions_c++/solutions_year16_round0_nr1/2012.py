#include <bits/stdc++.h>
using namespace std;

int t;

int n;
int tab[107];

void czys()
{
    for (int i=0; i<10; i++)
    {
        tab[i]=0;
    }
}

void rob(long long v)
{
    while(v)
    {
        tab[v%10]=1;
        v/=10;
    }
}

int czy()
{
    for (int i=0; i<10; i++)
    {
        if (!tab[i])
        {
            return 0;
        }
    }
    return 1;
}

int main()
{
    scanf("%d", &t);
    for (int tt=1; tt<=t; tt++)
    {
        scanf("%d", &n);
        //n=t;
        if (!n)
        {
            printf("Case #%d: INSOMNIA\n", tt);
            continue;
        }
        czys();
        for (long long i=1; 1; i++)
        {
            rob(i*n);
            if (czy())
            {
                printf("Case #%d: %lld\n", tt, i*n);
                break;
            }
        }
    }
    return 0;
}
