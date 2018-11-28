#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>

using namespace std;

int f[1005];

int main()
{
    freopen("x.in", "r", stdin);
    freopen("x.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        int n;
        scanf("%d", &n);
        int ans1 = 0, ans2 = 0, maxInteval = 0;
        for (int i = 0; i <n; i++)
            scanf("%d", &f[i]);
        for (int i = 1; i < n; i++)
        {
            ans1 += max(f[i - 1] - f[i], 0);
            maxInteval = max(maxInteval, f[i - 1] - f[i]);
        }
        int num = n - 1;
        for (int i = 0; i < n - 1; i++)
            if (f[i] < maxInteval)
            {
                ans2 += f[i];
                num--;
            }
        //cout<<ans2<<" "<<num<<" "<<maxInteval<<endl;
        printf("Case #%d: %d %d\n", cas, ans1, ans2 += num * maxInteval);
    }
    return 0;
}
