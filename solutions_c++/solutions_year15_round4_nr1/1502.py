#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cstring>
#include <string>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <cstdlib>
#include <iostream>

using namespace std;

#define FOR(i,l,r)  for(int i=(l); i<=(r); ++i)
#define REP(i,r)    for(int i=0; i<(r); ++i)
#define DWN(i,r,l)  for(int i=(r);i>=(l);--i)

#define pb push_back

typedef long long ll;
typedef pair<int, int>pii;

const int N = 110;

char str[N][N];

int l[N], r[N], u[N], d[N];
int num_r[N], num_c[N];
bool check(int n, int m) {
    REP(i, n)
        REP(j, m)
            if(str[i][j] != '.' && num_r[i] == 1 && num_c[j] == 1)  {
                return 0;
            }
    return 1;
}

int solve(int n, int m) {
    int ret = 0;
    REP(i, n)
        REP(j, m)
            if(str[i][j] != '.') {
                if(str[i][j] == '^')    if(u[j] == i)   ++ret;
                if(str[i][j] == 'v')    if(d[j] == i)   ++ret;
                if(str[i][j] == '<')    if(l[i] == j)   ++ret;
                if(str[i][j] == '>')    if(r[i] == j)   ++ret;
            }
    return ret;
}


int main() {
    freopen("A-large.in", "r", stdin);
    //freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int casnum;
    cin >> casnum;
    FOR(casid, 1, casnum) {
        memset(l, -1, sizeof(l));
        memset(r, -1, sizeof(r));
        memset(d, -1, sizeof(d));
        memset(u, -1, sizeof(u));
        memset(num_r, 0, sizeof(num_r));
        memset(num_c, 0, sizeof(num_c));
        int n, m;
        cin >> n >> m;

        REP(i, n)   scanf("%s", str[i]);
        REP(i, n)
            REP(j, m)
                if(str[i][j] != '.') {
                    if(l[i] == -1)  l[i] = r[i] = j;
                    else {
                        l[i] = min(l[i], j);
                        r[i] = max(r[i], j);
                    }

                    if(d[j] == -1)  d[j] = u[j] = i;
                    else {
                        u[j] = min(u[j], i);
                        d[j] = max(d[j], i);
                    }
                    ++num_c[j];
                    ++num_r[i];
                 }
        printf("Case #%d: ", casid);
        if(!check(n, m))    puts("IMPOSSIBLE");
        else cout << solve(n, m) << endl;
    }
    return 0;
}

