/*************************************************************************
    > File Name: C.cpp
    > Author: ALex
    > Mail: zchao1995@gmail.com 
    > Created Time: 2015年05月31日 星期日 00时20分57秒
 ************************************************************************/

#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <stack>
#include <map>
#include <bitset>
#include <set>
#include <bits/stdc++.h>

#include <vector>

using namespace std;

const double pi = acos(-1.0);
const int inf = 0x3f3f3f3f;
const double eps = 1e-15;
typedef long long LL;
typedef pair <int, int> PLL;

const int MAXM=200100;
const int MAXN=20000;
#define INF 0x5fffffff
map<string, int> mp;
vector<int> have[2010];
struct sap
{
    struct edge
    {
        int to, cap, next;
    } e[MAXM * 2];

    int p, head[MAXN], h[MAXN], vh[MAXN];
    int n, m, s, t, maxFlow;

    inline int min(int a, int b)
    {
        return a < b ? a : b;
    }
    inline void addedge(int a, int b, int c)
    {
        e[p].to = b, e[p].cap = c, e[p].next = head[a], head[a] = p++;
        e[p].to = a, e[p].cap = 0, e[p].next = head[b], head[b] = p++;
    }
    int dfs(int u, int pre)
    {
        if (u == t)
            return pre;
        int now, aug, mh = n + 10, to, tmp = pre;
        for (now = head[u]; now; now = e[now].next)
        {
            to = e[now].to;
            if (e[now].cap)
            {
                if (pre && h[u] == h[to] + 1)
                {
                    aug = dfs(to, min(pre, e[now].cap));
                    pre -= aug;
                    e[now].cap -= aug;
                    e[now ^ 1].cap += aug;
                    if (h[s] >= n)
                        return tmp - pre;
                }
                mh = min(mh, h[to]);
            }
        }
        if (tmp - pre > 0)
            return tmp - pre;
        --vh[h[u]];
        if (!vh[h[u]])
        {
            h[s] = n;
            return 0;
        }
        ++vh[h[u] = mh + 1];
        return 0;
    }

    void init()
    {
        maxFlow = 0;
        memset(h, 0, sizeof(h));
        memset(vh, 0, sizeof(vh));
        vh[0] = n;
    }
    void SAP()
    {
        init();
        while (h[s] < n)
            maxFlow += dfs(s, INF);
    }
    void pre(int nn, int ss = -1, int tt = -1)
    {
        p = 2;
        memset(head, 0, sizeof(head));
        n = nn;
        if(ss == -1) s = 0;
        else s = ss;
        if (tt == -1) t = n - 1;
        else t = tt;
    }
} g;

int main()
{
   // freopen("a.in", "r", stdin);
   // freopen("a.out", "w", stdout);
    int t, icase=1;
    scanf("%d", &t);
    while(t--)
    {
        int n;
        scanf("%d", &n);
        string str;
        getline(cin, str);
        mp.clear();
        int cnt = 2;
        for(int i = 0; i < n; i++)
        {
            getline(cin, str);
            istringstream is(str);
            string t;
            int arr[2000], larr = 0;
            while(is >> t)
            {
                map<string, int>::iterator it = mp.find(t);
                if(it == mp.end())
                    mp[t] = cnt++;
                arr[larr++] = mp[t];
            }
            sort(arr, arr + larr);
            larr = unique(arr, arr + larr) - arr;

            have[i].clear();
            for(int j = 0; j < larr; j++)
            {
                have[i].push_back(arr[j]);
            }
        }
        printf("Case #%d: ", icase++);
        int src = 0, sink = 1;
        g.pre(cnt + n, src, sink);
        g.addedge(src, cnt, INF);
        g.addedge(cnt + 1, sink, INF);

        for(int i = 0; i < n; i++)
            for(int j = 0; j < (int)have[i].size(); j++)
            {
                g.addedge(cnt + i, have[i][j], 1);
                g.addedge(have[i][j], cnt + i , 1);
            }
        g.SAP();
        printf("%d\n", g.maxFlow);
    }
    return 0;
}
