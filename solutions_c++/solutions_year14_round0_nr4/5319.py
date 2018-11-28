#include <cstdio>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <string>
#include <climits>
#include <cmath>
#include <queue>
#include <vector>
#include <stack>
#include <set>
#include <map>
#define INF 0x3f3f3f3f
#define eps 1e-8
using namespace std;

double a[100], b[100];
bool vis1[100], vis2[100];

int n;

int dfs1(int dep)
{
    if (dep == n)
    {
        return 0;
    }
    int tmp = 0;
    for (int j = n - 1; j >= 0; j --)
    {
        if (! vis2[j])
        {
            vis2[j] = true;
            int match = -1;
            for (int i = 0; i < n; i ++)
            {
                if (a[i] > b[j] && !vis1[i])
                {
                    vis1[i] = true;
                    match = i;
                    break;
                }
            }
            int ret = match == -1 ? 0 : 1;
            if (match == -1)
            {
                for(match = 0; vis1[match]; match ++)
                {
                    ;
                }
            }
            tmp = max(tmp, ret + dfs1(dep + 1));
            vis1[match] = false;
            vis2[j] = false;
        }
    }
    return tmp;
}

int dfs2(int dep)
{
    if (dep == n)
    {
        return 0;
    }
    int tmp = 0;
    for (int i = 0; i < n; i ++)
    {
        if (! vis1[i])
        {
            vis1[i] = true;
            int match = -1;
            for (int j = 0; j < n; j ++)
            {
                if (b[j] > a[i] && !vis2[j])
                {
                    vis2[j] = true;
                    match = j;
                    break;
                }
            }
            int ret = match == -1 ? 1 : 0;
            if (match == -1)
            {
                for(match = 0; vis2[match]; match ++)
                {
                    ;
                }
            }
            tmp = max(tmp, ret + dfs2(dep + 1));
            vis1[i] = false;
            vis2[match] = false;
        }
    }
    return tmp;
}

int main()
{
    freopen("D-small-attempt2.in", "r", stdin);
    freopen("D.out", "w", stdout);
    int cas;
    scanf("%d", &cas);
    for (int T = 1; T <= cas; T ++)
    {
        scanf("%d", &n);
        for (int i = 0; i < n; i ++)
        {
            scanf("%lf", &a[i]);
        }
        for (int i = 0; i < n; i ++)
        {
            scanf("%lf", &b[i]);
        }
        sort(a, a + n);
        sort(b, b + n);
        int ans1, ans2;
        memset(vis1, 0, sizeof(vis1));
        memset(vis2, 0, sizeof(vis2));
        ans1 = dfs1(0);
        memset(vis1, 0, sizeof(vis1));
        memset(vis2, 0, sizeof(vis2));
        ans2 = dfs2(0);
        printf("Case #%d: %d %d\n", T, ans1, ans2);
    }
    return 0;
}
