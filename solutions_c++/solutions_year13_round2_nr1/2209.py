#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <map>
#include <sstream>
#include <set>
#include <vector>
#include <string>
#include <queue>
#define INF 2100000000
#define eps 1e-8
#define lld long long

using namespace std;
int n, i, ans;
int a[2000];
void dfs(int sum, int x, int s)
{
    if (s > ans) return;
    if (x == n)
    {
        ans = min(ans, s);
        return;
    }
    if (sum > a[x])
    {
        dfs(sum + a[x], x + 1, s);
    }
    else
    {
        if (sum>1)dfs(sum * 2 - 1, x , s + 1);
        dfs(sum, x + 1, s + 1);
    }
}
int main()
{
    int tot = 0, T, v;
//    freopen("a.in","r",stdin);
//    freopen("a.out","w",stdout);
    cin>>T;
    while(T--)
    {
        scanf("%d%d", &v, &n);
        for(i = 0; i < n; i++)
            scanf("%d", &a[i]);
        sort(a, a + n);
        ans = INF;
        dfs(v, 0, 0);
        printf("Case #%d: %d\n", ++tot, ans);
    }
}
