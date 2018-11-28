/**
 * Copyright (c) 2014 Authors. All rights reserved.
 * 
 * FileName: D.cpp
 * Author: Beiyu Li <sysulby@gmail.com>
 * Date: 2014-05-31
 */
#include <bits/stdc++.h>

using namespace std;

#define REP(i,n) for (int i = 0; i < (n); ++i)
#define FOR(i,s,t) for (int i = (s); i <= (t); ++i)
#define FOREACH(i,c) for (__typeof(c.begin()) i = c.begin(); i != c.end(); ++i)

typedef long long LL;
typedef pair<int, int> Pii;

const int inf = 0x3f3f3f3f;
const LL infLL = 0x3f3f3f3f3f3f3f3fLL;

const int maxn = 200 + 5;
const int maxe = 200 + 5;

class Trie {
        int psz;
        struct Edge {
                int u, v, w;
                Edge *next;
        } epool[maxe], *e[maxn];
        int sz, val[maxn];

        Edge* add_edge(int u, int v, int w)
        {
                Edge *p = epool + psz++;
                p->u = u; p->v = v; p->w = w; p->next = e[u]; e[u] = p;
                return p;
        }

        Edge* find(int u, int c)
        {
                for (Edge *i = e[u]; i; i = i->next)
                        if (i->w == c) return i;
                return NULL;
        }

        int encode(char ch)
        {
                return ch - 'A';
        }

        public:
        void init()
        {
                psz = 0;
                memset(e, 0, sizeof(e));
                sz = 1;
                memset(val, -1, sizeof(val));
        }

        void insert(const char* s, int v)
        {
                int u = 0, n = strlen(s);
                for (int i = 0; i < n; ++i) {
                        int c = encode(s[i]);
                        Edge *p = find(u, c);
                        if (!p) p = add_edge(u, sz++, c);
                        u = p->v;
                }
                val[u] = v;
        }

        int query(const char* s)
        {
                int u = 0, n = strlen(s);
                for (int i = 0; i < n; ++i) {
                        int c = encode(s[i]);
                        Edge *p = find(u, c);
                        if (!p) return -1;
                        u = p->v;
                }
                return val[u];
        }

        int solve()
        {
                return sz;
        }
} trie[10];

int n, m, res, cnt;
char s[10][16];
int id[10];

void dfs(int dep)
{
        if (dep == n) {
                int tmp = 0;
                REP(j,m) {
                        bool found = false;
                        trie[j].init();
                        REP(i,n) if (id[i] == j) {
                                found = true;
                                trie[j].insert(s[i], 1);
                        }
                        if (found) tmp += trie[j].solve();
                }
                if (tmp > res) {
                        res = tmp;
                        cnt = 1;
                } else if (tmp == res) {
                        ++cnt;
                }
                return;
        }
        REP(j,m) {
                id[dep] = j;
                dfs(dep + 1);
        }
}

int main()
{
        int T, cas = 0;
        scanf("%d", &T);

        while (T--) {
                scanf("%d%d", &n, &m);
                REP(i,n) scanf("%s", s[i]);
                res = cnt = 0;
                dfs(0);
                printf("Case #%d: %d %d\n", ++cas, res, cnt);
        }

        return 0;
}
