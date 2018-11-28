#include <stdio.h>
#include <iostream>
using namespace std;

#define MAXN (1000+10)

int T, n;

int a[MAXN];
int f[MAXN], g[MAXN];

void doit()
{
    int ans;
    int l, r;

    scanf("%d", &n);
    for (int i = 1;i <= n;++i)
        scanf("%d", &a[i]);
    ans = n*n;

    ans = 0;
    l = 1; r = n;
    while (l < r)
    {
        int k = l;

        for (int i = l;i <= r;++i)
            if (a[i] < a[k]) k = i;
      //  printf("%d\n", k);
        if (k-l < r-k)
        {
            ans += k-l;
            for (int i = k; i > l;--i)
                a[i] = a[i-1];
            ++l;

        }
        else
        {
             ans += r-k;
            for (int i = k; i < r;++i)
                a[i] = a[i+1];
            --r;

        }
    }


    printf("%d\n", ans);

}

int main()
{
    freopen("B-large.in","r", stdin);
    freopen("B.out","w",stdout);
    scanf("%d", &T);
    for (int q = 1;q <= T;++q)
    {
        printf("Case #%d: ", q);
        doit();
    }
    return 0;

}
