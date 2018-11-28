#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <cstring>
#include <algorithm>
#include <string>
#include <set>
#include <functional>
#include <numeric>
#include <sstream>
#include <stack>
#include <map>
#include <queue>

#define CL(arr, val)    memset(arr, val, sizeof(arr))
#define REP(i, n)       for((i) = 0; (i) < (n); ++(i))
#define FOR(i, l, h)    for((i) = (l); (i) <= (h); ++(i))
#define FORD(i, h, l)   for((i) = (h); (i) >= (l); --(i))
#define L(x)    (x) << 1
#define R(x)    (x) << 1 | 1
#define MID(l, r)   (l + r) >> 1
#define Min(x, y)   (x) < (y) ? (x) : (y)
#define Max(x, y)   (x) < (y) ? (y) : (x)
#define E(x)        (1 << (x))
#define iabs(x)     (x) < 0 ? -(x) : (x)
#define OUT(x)  printf("%lld\n", x)
#define Read()  freopen("data.in", "r", stdin)
#define Write() freopen("data.out", "w", stdout);

typedef long long LL;
const double eps = 1e-6;
const double PI = acos(-1.0);
const int inf = 0x1F1F1F1F;

using namespace std;

struct node {
    int i, j;
    int val;
    node() {}
    node(int a, int b, int v) : i(a), j(b), val(v) {}
    bool operator < (const node b) const {
        return val > b.val;
    }
}u;

priority_queue<node> q;

bool visr[110], visc[110];
int mp[110][110];

int main() {

    Read();
    Write();

    int T, i, j, n, m;
    int cas = 0;
    bool f1, f2;
    scanf("%d", &T);
    while(T--) {
        scanf("%d%d", &n, &m);
        while(!q.empty())   q.pop();
        f1 = true;
        for(i = 0; i < n; ++i) {
            for(j = 0; j < m; ++j) {
                scanf("%d", &mp[i][j]);
                if(mp[i][j] > 10 && mp[i][j] < 100) f1 = false;
                q.push(node(i, j, mp[i][j]));
            }
        }

        CL(visr, 0);
        CL(visc, 0);

        while(!q.empty()) {
            u = q.top(); q.pop();
            if(visr[u.i] && visc[u.j])  continue;

            f1 = true;
            for(i = 0; i < n && f1; ++i) {
                if(mp[i][u.j] > mp[u.i][u.j])   f1 = false;
            }
            if(f1)   visc[u.j] = true;

            f2 = true;
            for(j = 0; j < m && f2; ++j) {
                if(mp[u.i][j] > mp[u.i][u.j])   f2 = false;
            }
            if(f2)   visr[u.i] = true;
            if(!f1 && !f2)  break;
        }

        bool f = true;

        for(i = 0; i < n; ++i) {
            if(visr[i] == false)    {f = false; break;}
        }
        for(j = 0; j < m; ++j) {
            if(visc[j] == false)    {f = false; break;}
        }

        if(f)    printf("Case #%d: YES\n", ++cas);
        else    printf("Case #%d: NO\n", ++cas);
    }
    return 0;
}
