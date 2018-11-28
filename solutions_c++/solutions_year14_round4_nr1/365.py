#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int X,N,s[10005];

void solve()
{
    scanf("%d%d", &N, &X);
    for (int i=0;i<N;++i)
        scanf("%d", &s[i]);
    sort(s,s+N);
    int p=0,q=N-1;
    int ans = 0;
    while(p<=q)
    {
        if (p==q)
        {
            ans ++;
            break;
        }
        if (s[q]+s[p]>X)
        {
            ans ++;
            q--;
        }
        else
        {
            ans++;
            p++;q--;
        }
    }
    printf(" %d\n", ans);
}

int main()
{
//    freopen("A-large.in","r",stdin);
//    freopen("A-large.out","w",stdout);
    int ln_t;
    scanf("%d", &ln_t);
    for (int ln_cas=1;ln_cas<=ln_t;++ln_cas)
    {
        printf("Case #%d:", ln_cas);
        solve();
    }
    return 0;
}
