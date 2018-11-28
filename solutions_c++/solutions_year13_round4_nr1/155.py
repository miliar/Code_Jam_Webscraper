#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <math.h>
#include <vector>
#include <deque>
#include <string>
#include <string.h>
#include <queue>
#include <stdlib.h>
#include <set>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

const ll MOD = 1000002013LL;

struct cell {
    ll x, y;

    bool operator <(const cell& A) const {
        return x < A.x;
    }
};

int main() {
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);

    int _T;
    scanf("%d\n", &_T);

    for (int __test = 1; __test <= _T; ++__test) {
        ll n, m;
        cin >> n >> m;

        vector<pair<ll, ll> > events;
        ll ans = 0, cans = 0;
        for (int i = 0; i < m; ++i) {
            ll o, e, p;
            cin >> o >> e >> p;
            events.push_back(make_pair(o, -p));
            events.push_back(make_pair(e, p));

            ll len = (e - o);
            ll always = (((len * n) % MOD) * p) % MOD;
            ll cool = (len * (len - 1)) / 2;
            cool %= MOD;
            cool *= p;
            cool %= MOD;
            cans = (cans + (always - cool + MOD)) % MOD; 
            ans = (ans + always) % MOD; 
        }
        sort(events.begin(), events.end());

        priority_queue<cell> q;
        for (int i = 0; i < events.size(); ++i) {
            events[i].second = -events[i].second;
            if (events[i].second > 0) {
                cell T;
                T.x = events[i].first;
                T.y = events[i].second;
                q.push(T);
            } else {
                ll need = -events[i].second;
                while (need > 0) {
                    cell T = q.top(); q.pop();
                    ll len = events[i].first - T.x;
                    ll cool;
                    cool = (len * (len - 1)) / 2;
                    cool %= MOD;
                    if (T.y > need) {
                        cool *= need;
                        cool %= MOD;
                        ans = (ans + MOD - cool) % MOD;
                        T.y -= need;
                        q.push(T);
                        break;
                    } else {
                        cool *= T.y;
                        cool %= MOD;
                        ans = (ans + MOD - cool) % MOD;
                        need -= T.y;
                    }
                }
            }
        }

        printf("Case #%d: ", __test);
        cout << (cans - ans + MOD) % MOD << endl;
    }


    return 0;
}

