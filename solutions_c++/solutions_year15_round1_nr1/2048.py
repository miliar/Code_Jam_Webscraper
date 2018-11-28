#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <string>
#include <sstream>
#define INF 2100000000
#define mod 100007
using namespace std;
int a[1111];
int main()
{
    int T, cas = 0, n, i, j;
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    cin>>T;
    while(T--)
    {
        scanf("%d", &n);
        for(i = 0; i < n; i++)
            scanf("%d", &a[i]);
        int ans1, ans2;
        ans1 = ans2 = 0;
        for(i = 1; i < n; i++){
            if (a[i] < a[i - 1]) ans1 += a[i - 1] - a[i];
        }
        int maxp = 0;
        for(i = 1; i < n; i++){
            if (a[i] < a[i - 1]) maxp = max(maxp, a[i - 1] - a[i]);
        }
            int sum = 0;
            for(i = 1; i < n; i++){
                int t = 0;
                t = a[i - 1];
                sum += min(t, maxp);
            }
            ans2 = sum;

        printf("Case #%d: %d %d\n", ++cas, ans1, ans2);
    }
    return 0;
}
