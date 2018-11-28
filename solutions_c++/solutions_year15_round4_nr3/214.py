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
#include <sstream>

using namespace std;

#define x first
#define y second
#define mp make_pair
#define pb push_back
#define sz(X) ((int)((X).size()))

const double eps = 1e-8;

const int N = 5000005;

int now[N], ne[N], next[N], key[N], point[N];
int vd[N], d[N], pos[N], ed, s, t;
bool gap;
map<string, int> Map;

void add(int a, int b, int c)
{
    ++ed; next[now[a]] = ed; now[a] = ed;
    point[ed] = b; key[ed] = c; next[ed] = 0; pos[ed] = ed + 1;
    ++ed; next[now[b]] = ed; now[b] = ed;
    point[ed] = a; key[ed] = 0; next[ed] = 0; pos[ed] = ed - 1;
}

int getId(string s)
{
    if (Map.count(s)) return Map[s];
    int x = sz(Map) + 1;
    Map[s] = x;
    add(x, x + 4000, 1);
    return x;
}

int dfs(int a, int flow)
{
    if (a == t) return flow;
    int ret = 0;
    for (int i = ne[a]; i; i = next[i], ne[a] = i)
    {
        int j = point[i];
        int k = min(flow, key[i]);
        if (d[a] == d[j] + 1 && k)
        {
            int tmp = dfs(j, k);
            key[i] -= tmp;
            key[pos[i]] += tmp;
            flow -= tmp;
            ret += tmp;
        }
        if (flow == 0) return ret;
    }
    --vd[d[a]];
    if (vd[d[a]] == 0) gap = true;
    ++d[a];
    ++vd[d[a]];
    return ret;
}

void work()
{
    Map.clear();
    int n;
    cin >> n;
    string ss, sss;
    getline(cin, ss);
    s = 8001;
    t = 8002;
    ed = t;
    for (int i = 1; i <= ed; ++i)
        now[i] = i, next[i] = 0;
    for (int i = 0; i < n; ++i)
    {
        getline(cin, ss);
        istringstream sin(ss);
        vector<int> a;
        while (sin >> sss)
        {
            int x = getId(sss);
            a.pb(x);
            if (i == 0) add(s, x, 10000000);
            if (i == 1) add(x + 4000, t, 10000000);
        }
        for (int j = 0; j < sz(a); ++j)
            for (int k = 0; k < sz(a); ++k)
                if (j != k)
                    add(a[j] + 4000, a[k], 10000000);
    }
    for (int i = 1; i <= t; ++i)
        d[i] = vd[i] = 0;
    vd[0] = t;
    int ans = 0;
    gap = false;
    while (d[s] < t)
    {
        for (int i = 1; i <= t; ++i)
            ne[i] = next[i];
        ans += dfs(s, 10000000);
        if (gap) break;
    }
    cout << ans << endl;
}

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
//    ios_base::sync_with_stdio(false);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t)
    {
        cerr << t << endl;
        printf("Case #%d: ", t);
        work();
    }
}
