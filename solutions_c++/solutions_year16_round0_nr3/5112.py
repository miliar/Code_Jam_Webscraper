#include <iostream>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <queue>
#include <cassert>
#include <map>
#include <set>
#include <ctime>
#include <unordered_map>

using namespace std;

#define x first
#define y second
#define mp make_pair
#define pb push_back
#define sz(X) ((int)((X).size()))

const double eps = 1e-10;
const int inf = 1000000000;

const int N = 100005;
const int mo = 1000000000 + 7;

int n, m;
vector<char> s;
vector<long long> b;

void dfs(int dep, vector<long long> a)
{
    if (m == 0) return;
    if (dep == 0)
    {
        for (int i = 0; i < 9; ++i)
        {
            bool flag = true;
            for (int j = 2; j <= 1000 && j < a[i]; ++j)
                if (a[i] % j == 0)
                {
                    b[i] = j;
                    flag = false;
                    break;
                }
            if (flag) return;
        }
        for (int i = 0; i < sz(s); ++i)
            cout << s[i];
        for (int i = 0; i < 9; ++i)
            cout << ' ' << b[i];
        cout << endl;
        --m;
        return;
    }
    for (int i = 0; i < 9; ++i)
        a[i] *= (i + 2);
    if (dep > 1)
    {
        s.pb('0');
        dfs(dep - 1, a);
        s.pop_back();
    }
    for (int i = 0; i < 9; ++i)
        a[i] += 1;
    s.pb('1');
    dfs(dep - 1, a);
    s.pop_back();
}

void work()
{
    cin >> n >> m;
    vector<long long> a;
    for (int i = 0; i < 9; ++i)
    {
        a.pb(1);
        b.pb(1);
    }
    s.pb('1');
    dfs(n - 1, a);
}

int main()
{
    #ifdef LOCAL_TEST
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i)
    {
        printf("Case #%d:\n", i);
        work();
    }
    return 0;
}
