#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <cstring>
#include <string>

using namespace std;

typedef long long ll;

int test;
int e, r, n;
int v[10010], id[10010];
int used[10010];
int t[10010];
int mr1[10010], mr2[10010];
set<int> fr, fl;

inline int cmp(const int a, const int b) {
    return v[a] > v[b];
}

int main() {
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    scanf("%d", &test);
    for(int ttest = 1; ttest <= test; ttest++) {
        scanf("%d%d%d", &e, &r, &n);
        ll ret = 0;
        mr1[0] = mr1[n+1] = 0;
        mr2[0] = mr2[n+1] = e;
        for(int i = 1; i <= n; i++) {
            scanf("%d", &v[i]);
            id[i] = i;
            mr1[i] = 0;
            mr2[i] = e;
        }
        sort(id+1, id+1+n, cmp);
        fr.clear(); fl.clear();
        fr.insert(n+1);
        fl.insert(0);
        memset(used, 0, sizeof used);
        int m = 0;
        for(int ii = 1; ii <= n; ii++) {
            int i = id[ii];
            int ir = (*fr.upper_bound(i));
            int il = -(*fl.upper_bound(-i));
            
            int le = 0, ri = e;
            while (le+1 < ri) {
                int mid = (le+ri)/2;
                if (mr2[il] + (i-il)*r >= mid && min(mr2[il] + (i-il)*r, e)-mid + (ir-i)*r >= used[ir]+mr1[ir]) le = mid;
                else ri = mid;
            }
            if (mr2[il] + (i-il)*r >= ri && min(mr2[il] + (i-il)*r, e)-ri + (ir-i)*r >= used[ir]+mr1[ir]) le = ri;
            ret += ll(le) * v[i];
            used[i] = le;
            mr1[i] = max(mr1[i], used[ir]+mr1[ir] - (ir-i)*r);
            mr2[i] = min(e-used[i], mr2[il] + (i-il)*r-used[i]);
            fr.insert(i);
            fl.insert(-i);
        }
        printf("Case #%d: %lld\n", ttest, ret);
    }    
    return 0;
    
}
