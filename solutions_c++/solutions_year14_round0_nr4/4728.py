#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <fstream>
using namespace std;
double e = 0.0000001;
double a[1024], b[1024];
int n, cases;
bool check(int pos)
{
    for(int i = pos, j = 1; i<= n; i++, j++)
        if(b[j]-a[i]>=e) return 0;
    return 1;
}
int main() {
    freopen("D.in", "r", stdin);
    freopen("D.out", "w", stdout);
    scanf("%d", &cases);
    for(int t = 1; t <= cases; t++)
    {
        scanf("%d", &n);
        int cnt=n, ans = n;
        for(int i = 1; i <= n; i++)
            scanf("%lf", &a[i]);
        sort(a+1, a+n+1);
        for(int i = 1; i <= n; i++)
            scanf("%lf", &b[i]);
        sort(b+1,b+n+1);
        for(int i = 1, j = 1; i<=n && j<=n; i++)
            {
                while(a[i]-b[j]>=e && j<=n)
                    j++;
                if(j>n)  break;
                cnt--;j++;
            }
        for(int i = 1; i<=n; i++, ans--)
         if(check(i)) break;
        printf("Case #%d: %d %d\n",t,ans,cnt);
    }
    return 0;
}
