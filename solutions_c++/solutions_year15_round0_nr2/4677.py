#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
#define N 105
vector<int> p;
bool q[N];
bool qq[N];
int n, ans;

bool check()
{
    for (int i = 0; i < p.size(); ++i)
    {
        if (p[i] > 0)
            return 0;
    }
    return 1;
}

void dfs(int k)
{
    if (check())
    {
        if (k < ans)
        {
            ans = k;
            // memcpy(qq, q, sizeof(qq));
        }
        return;
    }
    for (int i = 0; i < p.size(); ++i)
        --p[i];
    // q[k] = 0;
    dfs(k + 1);
    int j = 0;
    for (int i = 0; i < p.size(); ++i)
    {
        ++p[i];
        if (p[i] > p[j])
            j = i;
    }
    if (p[j] == 9)
    {
        p[j] = 3;
        p.push_back(3);
        p.push_back(3);
        dfs(k + 2);
        p.pop_back();
        p.pop_back();
        p[j] = 9;
    }
    if (p[j] > 1)
    {
        int m = p[j];
        p[j] = m / 2;
        p.push_back(m - m / 2);
        // q[k] = 1;
        dfs(k + 1);
        p.pop_back();
        p[j] = m;
    }
}

int solve()
{
    scanf("%d", &n);
    p.clear();
    for (int i = 0; i < n; ++i)
    {
        int k;
        scanf("%d", &k);
        p.push_back(k);
    }
    sort(p.begin(), p.end());
    ans = p[n - 1];
    dfs(0);
    return ans;
}

int main()
{
    int t;
    freopen("1.txt", "r", stdin);
    freopen("2.txt", "w", stdout);
    scanf("%d", &t);
    for (int tt = 1; tt <= t; ++tt)
    {
        printf("Case #%d: ", tt);
        printf("%d\n", solve());
        // for (int i = 0; i < ans; ++i)
        // {
        //     printf("%d ", qq[i]);
        // }
        // puts("");
    }
    return 0;
}