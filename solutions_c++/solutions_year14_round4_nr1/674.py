#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;

#define MAXN (10000+10)

int T, n, m;
int a[MAXN];

void doit()
{
    int ans = 0;

    scanf("%d%d", &n, &m);
    for (int i = 0;i < n;++i)
        scanf("%d", &a[i]);
    sort(a, a+n);
    int l = 0;
    int i = n-1;
    while (i >= l)
    {
        ++ans;
        if (a[i]+a[l] <= m)
            ++l;
        --i;
    }
    printf("%d\n", ans);
}

int main()
{
    freopen("A-large.in","r", stdin);
    freopen("A.out","w", stdout);
    scanf("%d", &T);
    for (int q = 1;q <= T;++q)
    {
        printf("Case #%d: ", q);
        doit();
    }

}
