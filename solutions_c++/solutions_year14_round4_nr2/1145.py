#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int result;
bool used[1024];

void dfs(int n, int dep, int max_deep, int last, int sta[], int a[])
{
    if (dep == max_deep)
    {
        int cnt = 0;
        vector<int> ret;
        for (int i = 0; i < n; ++i)
            ret.push_back(a[i]);
        for (int i = 0; i < max_deep; ++i)
        {
            int p = find(ret.begin(), ret.end(), sta[i]) - ret.begin();
            while (p != i)
            {
                swap(ret[p], ret[p - 1]);
                --p;
                ++cnt;
            }
        }
        int pos = max_deep;
        for (int i = n - 1; i >= 0; --i)
        {
            if (used[i])
                continue;
            int p = find(ret.begin(), ret.end(), i) - ret.begin();
            while (p != pos)
            {
                swap(ret[p], ret[p - 1]);
                --p;
                ++cnt;
            }
            ++pos;
        }
        result = min(result, cnt);
    }
    else 
    {
        for (int i = last; i < n - 1; ++i)
        {
            sta[dep] = i;
            used[i] = true;
            dfs(n, dep + 1, max_deep, i + 1, sta, a);
            used[i] = false;
        }
    }
}

void Solved(int nT)
{
    int n, a[1024], sta[1024];
    vector<int> b;
    cin >> n;
    for (int i = 0; i < n; ++i)
    {
        cin >> a[i];
        b.push_back(a[i]);
    }
    result = 0x3f3f3f3f;
    memset(used, false, sizeof(used));
    sort(b.begin(), b.end());
    for (int i = 0; i < n; ++i)
        a[i] = lower_bound(b.begin(), b.end(), a[i]) - b.begin();
    for (int m = 0; m < n; ++m)
        dfs(n, 0, m, 0, sta, a);
    printf("Case #%d: %d\n", nT, result);
}

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);

    int T = 1;
    cin >> T;
    for (int nT = 1; nT <= T; ++nT)
    {
        Solved(nT);
    }

    return 0;
}