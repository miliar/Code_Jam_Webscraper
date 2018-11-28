#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <queue>

using namespace std;
typedef long long ll;
typedef pair <int, int> pii;

vector <int> a;

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tests;
    scanf("%d", &tests);
    for (int t = 1; t <= tests; t++)
    {
        int n, x;
        scanf("%d %d", &n, &x);
        int ans = 0;
        a.clear();
        for (int i = 0; i < n; i++)
        {
            int o;
            scanf("%d", &o);
            a.push_back(o);
        }
        sort(a.begin(), a.end());
        int l = 0, r = a.size() - 1;
        while (l <= r)
        {
            if (l == r)
            {
                ans++;
                l++, r--;
                continue;
            }
            if (a[l] + a[r] <= x)
            {
                ans++;
                l++, r--;
                continue;
            }
            ans++;
            r--;
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
