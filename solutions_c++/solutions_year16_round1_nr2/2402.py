#include <iostream>
#include <cstdio>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <utility>
#include <ctime>
#include <cassert>

#define F first
#define S second
#define pb push_back
#define mp make_pair

using namespace std;

typedef long long ll;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;

const int maxn = (int)1e2 + 10;
const int inf = (int)1e9;
const int mod = (int)1e9 + 7;
const ll INF = (ll)1e18;
const double eps = (int)1e-9;

int was[maxn], used[maxn], a[maxn][maxn], row[maxn], n;

bool isGreater(int u, int v)
{
    for (int i = 0; i < n; ++i)
        if (a[u][i] <= a[v][i]) return false;
    return true;
}

bool check(int cnt)
{
    for (int i = 0; i < 2 * n - 1; ++i)
        was[i] = false;
    
    int chance = 2;
    
    for (int i = 0; i < n; ++i)
    {
        bool flag = false;
        for (int j = 0; j < 2 * n - 1; ++j)
        {
            if (used[j] || was[j]) continue;
            
            bool ok = true;
            for (int k = 0; k < cnt; ++k)
                if (a[j][k] != a[row[k]][i])
                {
                    ok = false;
                    break;
                }
            
            if (ok)
            {
                was[j] = true;
                flag = true;
                break;
            }
        }
        if (!flag) --chance;
        if (!chance) return false;
    }
    return true;
}

void findAnswer()
{
    for (int i = 0; i < n + n - 1; ++i)
        was[i] = false;
    
    for (int i = 0; i < n; ++i)
    {
        bool flag = false;
        for (int j = 0; j < 2 * n - 1; ++j)
        {
            if (used[j] || was[j]) continue;
            
            bool ok = true;
            for (int k = 0; k < n; ++k)
                if (a[j][k] != a[row[k]][i]) ok = false;
            
            if (ok)
            {
                was[j] = true;
                flag = true;
                break;
            }
        }
        if (!flag)
        {
//            for (int i = 0; i < n; ++i, cout << endl)
//                for (int j = 0; j < n; ++j)
//                    printf("%d ", a[row[i]][j]);
            for (int j = 0; j < n; ++j)
                printf("%d ", a[row[j]][i]);
            return;
        }
    }
    return;
}

bool rec(int v)
{
    if (v == n)
    {
        findAnswer();
        return true;
    }
    for (int i = 0; i < 2 * n - 1; ++i)
    {
        if (used[i]) continue;
        row[v] = i;
        used[i] = true;
        if (!v)
        {
            if (check(v + 1) && rec(v + 1))
            {
                used[i] = false;
                return true;
            }
        }
        else if (isGreater(i, row[v - 1]) && check(v + 1) && rec(v + 1))
        {
            used[i] = false;
            return true;
        }
        used[i] = false;
    }
    return false;
}

int main()
{
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
    {
        scanf("%d", &n);
        for (int j = 0; j < 2 * n - 1; ++j)
            for (int k = 0; k < n; ++k)
                scanf("%d", &a[j][k]);
        
        printf("Case #%d: ", i + 1);
        rec(0);
        puts("");
    }
    return 0;
}