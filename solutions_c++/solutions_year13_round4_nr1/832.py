// =====================================================================================
// 
//       Filename:  aa.cc
// 
//    Description:  greedy
// 
//        Version:  1.0
//        Created:  2013年06月01日 23时48分29秒
//       Revision:  none
//       Compiler:  g++
// 
//         Author:  Boyang Yang (barty), maiL@barty.ws
//        Company:  http://barty.ws
// 
// =====================================================================================


#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
using namespace std;

typedef long long LL;

template <typename T> void checkMin(T &a, const T &b) { if (b < a) a = b; }
template <typename T> void checkMax(T &a, const T &b) { if (b > a) a = b; }

struct seg {
    LL x, y, p;
    bool LLer(seg a) {
        LL min1 = min(x, y), max1 = max(x, y), min2 = min(a.x, a.y), max2 = max(a.x, a.y);
        if (min1 > min2) {
            swap(min1, min2);
            swap(max1, max2);
        }
        return (max1 >= min1);
    }
} d[1010];

const LL module = 1000002013LL;

LL fa[1010], n, m;
LL father(LL v) {
    if (fa[v] != v) fa[v] = father(fa[v]);
    return fa[v];
}
void pack(LL x, LL y) {
    LL fx = father(x), fy = father(y);
    if (fx != fy) fa[fx] = fy;
}

LL gao(LL x, LL y) {
    LL dis = abs(x - y);
    if (dis == 0) return 0;
    return ((n * 2 - dis + 1) * dis / 2) % module;
}

pair<LL, LL> in[1023], out[1023];

int main (int argc, char *argv[]) {
    LL T;
    scanf("%lld", &T);
    for (LL ca = 1; ca <= T; ++ca) {
        scanf("%lld%lld", &n, &m); 
        for (LL i = 1; i <= m; ++i) fa[i] = i;
        LL tot = 0;
        for (LL i = 1; i <= m; ++i) {
            scanf("%lld%lld%lld", &d[i].x, &d[i].y, &d[i].p);

            tot = (tot + gao(d[i].x, d[i].y) * d[i].p) % module;
        }
        for (LL i = 1; i <= m; ++i)
            for (LL j = i + 1; j <= m; ++j)
                if (d[i].LLer(d[j])) pack(i, j);
        for (LL i = 1; i <= m; ++i)
            fa[i] = father(fa[i]);
        LL ans = 0;
        for (LL i = 1; i <= m; ++i) {
            LL cnt = 0;
            for (LL j = 1; j <= m; ++j)
                if (fa[j] == i) {
                    in[cnt] = make_pair(d[j].x, d[j].p);
                    out[cnt] = make_pair(d[j].y, d[j].p);
                    ++cnt;
                }
            sort(in, in + cnt);
            sort(out, out + cnt);
            for (LL j = cnt - 1, k = cnt - 1; j >= 0; --j) {
                while (k > 0 && out[k-1].first >= in[j].first) --k;
                LL temp = k;
                while (in[j].second) {
                    LL delta = min(in[j].second, out[temp].second);
                    in[j].second -= delta;
                    out[temp].second -= delta;
                    ans = (ans + delta * gao(in[j].first, out[temp].first)) % module;
                    ++temp;
                }
            }
        }
        printf("Case #%lld: %lld\n", ca, ((tot - ans) % module + module)%module);
    }
    return 0;
}
