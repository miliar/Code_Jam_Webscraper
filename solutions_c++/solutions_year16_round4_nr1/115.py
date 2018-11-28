/**
 * Copyright © 2016 Authors. All rights reserved.
 * 
 * FileName: A.cpp
 * Author: Beiyu Li <sysulby@gmail.com>
 * Date: 2016-05-28
 */
#include <bits/stdc++.h>

using namespace std;

#define rep(i,n) for (int i = 0; i < (n); ++i)
#define For(i,s,t) for (int i = (s); i <= (t); ++i)
#define foreach(i,c) for (__typeof(c.begin()) i = c.begin(); i != c.end(); ++i)

typedef long long LL;
typedef pair<int, int> Pii;

const int inf = 0x3f3f3f3f;
const LL infLL = 0x3f3f3f3f3f3f3f3fLL;

const int maxn = 12 + 5;
const char* str = "RPS";

string f[maxn][3];

void init()
{
        rep(i,3) f[0][i] = str[i];
        For(i,1,12) rep(j,3) {
                int k = (j + 2) % 3;
                if (f[i-1][j] < f[i-1][k]) f[i][j] = f[i-1][j] + f[i-1][k];
                else f[i][j] = f[i-1][k] + f[i-1][j];
        }
}

bool check(const string& t, int r, int p, int s)
{
        foreach(it,t) {
                if (*it == 'R' && !r--) return false;
                if (*it == 'P' && !p--) return false;
                if (*it == 'S' && !s--) return false;
        }
        return true;
}

int main()
{
        int T, cas = 0;
        scanf("%d", &T);

        init();
        while (T--) {
                int n, r, p, s;
                scanf("%d%d%d%d", &n, &r, &p, &s);
                check("NP", r, p, s);
                string ret = "impossible";
                rep(j,3) if (check(f[n][j], r, p, s)) ret = min(ret, f[n][j]);
                printf("Case #%d: %s\n", ++cas, ret[0] == 'i'?
                                "IMPOSSIBLE": ret.c_str());
        }

        return 0;
}
