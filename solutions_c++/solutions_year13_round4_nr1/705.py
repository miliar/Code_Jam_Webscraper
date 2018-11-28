//============================================================================
// Name        : gcj.cpp
// Author      : ronaflx
// Version     : 1.0
// Copyright   : GNU GPL
// Description : 
//============================================================================

#include <cstdio>
#include <cstring>
#include <vector>
#include <set>
#include <algorithm>
#include <queue>
using namespace std;

typedef long long LL;
const LL MOD = 1000002013; 
struct passager {
    LL o, e, p;
};

bool operator < (const passager& a, const passager& b) {
    return a.o == b.o ? a.e < b.e : a.o < b.o;
}

LL cost(LL from, LL to, LL p, LL n) {
    LL s = to - from;
    return ((n + n - s + 1) * s / 2 % MOD) * p % MOD;
}
int main() {
    int t, n, m, s;
    scanf("%d", &t);
    for(int cas = 1;cas <= t;cas++) {
        scanf("%d %d", &n, &m);
        vector<passager> pass(m);
        vector<LL> station;
        LL ori = 0, res = 0;
        for(int i = 0;i < m;i++) {
            scanf("%lld %lld %lld", &pass[i].o, &pass[i].e, &pass[i].p);
            station.push_back(pass[i].o);
            station.push_back(pass[i].e);
            ori += cost(pass[i].o, pass[i].e, pass[i].p, n);
            ori %= MOD;
        }
        sort(station.begin(), station.end());
        station.erase(unique(station.begin(), station.end()), station.end());
        s = int(station.size());
        vector<LL> pi(s), po(s);
        for(int i = 0;i < m;i++) {
            int pii = lower_bound(station.begin(), station.end(), pass[i].o) - station.begin();
            int poi = lower_bound(station.begin(), station.end(), pass[i].e) - station.begin();
            pi[pii] += pass[i].p, po[poi] += pass[i].p;
        }
        priority_queue<pair<LL, LL> > pq;
        for(int i = 0;i < s;i++) {
            LL j = station[i];
            if(pi[i]) {
                pq.push(make_pair(j, pi[i]));
            }
            while(po[i] != 0) {
                pair<LL, LL> p = pq.top();
                pq.pop();
                if(p.second > po[i]) {
                    res += cost(p.first, j, po[i], n);
                    p.second -= po[i];
                    po[i] = 0;
                    pq.push(p);
                } else {
                    res += cost(p.first, j, p.second, n);
                    po[i] -= p.second;
                }
                res %= MOD;
            }
        }
        printf("Case #%d: %lld\n", cas, (ori + MOD - res) % MOD);
    }
    return 0;
}
