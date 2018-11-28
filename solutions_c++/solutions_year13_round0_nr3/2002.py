//Przemysław Jakub Kozłowski
#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
typedef long long LL;
const int W = 10000007;

int pier(LL x)
{
    int p = 1, k = min(x, (LL)W)+1, sr;

    while(p < k)
    {
        sr = (p+k)/2;
        if((LL)sr*sr < x) p = sr+1;
        else k = sr;
    }
    return k;
}

bool pal(LL x)
{
    LL rx = 0, tmpx = x;

    while(tmpx > 0)
    {
        rx = rx*10+(tmpx%10);
        tmpx /= 10;
    }
    return x == rx;
}

int t;
int tab[W+7];

int main()
{
    scanf("%d", &t);

    for(int i = 1;i <= W;i++)
    {
        tab[i] = tab[i-1];
        if(pal(i) && pal((LL)i*i))
        {
            tab[i]++;
            //cerr << "Liczba: " << i << endl;
        }
    }

    for(int ti = 1;ti <= t;ti++)
    {
        LL a,b;

        scanf("%lld%lld", &a, &b);

        int c = pier(a);
        int d = pier(b);
        if((LL)d*d > b) d--;

        printf("Case #%d: %d\n", ti, tab[d]-tab[c-1]);
    }

    return 0;
}
