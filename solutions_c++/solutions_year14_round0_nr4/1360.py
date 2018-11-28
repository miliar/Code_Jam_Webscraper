#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;

int T, n;
double a[10000], b[10000];

void doit()
{
    int ans1, ans2;
    int l, r;

    scanf("%d", &n);
    for (int i = 0;i < n;++i)
        scanf("%lf", &a[i]);
    for (int i = 0;i < n;++i)
        scanf("%lf", &b[i]);
    sort(a, a+n);
    sort(b, b+n);

    ans1 = ans2 = 0;
    l = 0; r = n-1;
    for (int i = 0;i < n;++i)
    {
        if (a[i] > b[l])
        {
            ++ans1;
            ++l;
        }
        else --r;
    }

    l = 0;
    for (int i = 0;i < n;++i)
    {
        while (l < n && b[l] < a[i]) ++l;
        if (l >= n) ++ans2;
        else ++l;
    }
    printf("%d %d\n", ans1, ans2);

}

int main()
{
    freopen("D-large.in","r", stdin);
    freopen("D-large.out","w",stdout);
    scanf("%d", &T);
    for (int q = 1;q <= T;++q)
    {
        printf("Case #%d: ", q);
        doit();
    }
    return 0;
}
