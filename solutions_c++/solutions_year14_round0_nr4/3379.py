#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int T,n,ans1,ans2;
bool h[1111];
double a[1111],b[1111];

int main()
{
    freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);
    scanf("%d", &T);
    for (int tt = 0; tt < T; tt++)
    {
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
            scanf("%lf", &a[i]);
        sort(a, a+n);
        for (int i = 0; i < n; i++)
            scanf("%lf", &b[i]);
        sort(b, b+n);
        ans1 = 0;
        memset(h, false, sizeof h);
        for (int i = 0; i < n; i++)
        {
            bool ok = false;
            for (int j = 0; j < n; j++)
                if (!h[j] && b[j] > a[i])
                {
                    h[j] = ok = true; break;
                }
            if (!ok) ans1++;
        }
        ans2 = 0;
        int la = 0, ra = n - 1;
        int lb = 0, rb = n - 1;
        while (la <= ra)
        {
            if (a[ra] > b[rb])
            {
                ans2++; ra--; rb--; continue;
            }
            la++; rb--;
        }
        printf("Case #%d: %d %d\n", tt+1, ans2, ans1);
    }
}
