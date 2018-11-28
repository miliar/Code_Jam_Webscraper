#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <map>
#include <set>
#include <stack>
#include <vector>
#include <algorithm>
#include <utility>
#include <memory.h>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

const LL MOD = 1000002013;

LL n;
LL m;

LL Cost(LL len) {
    return (n * 2 - len + 1) * len / 2;
}

struct Event {
    LL pos;
    LL act;
    LL cnt;

    Event(LL pos = 0, LL act = 0, LL cnt = 0)
        : pos(pos), act(act), cnt(cnt)
    { }

    bool operator<(const Event& rhs) const {
        return pos < rhs.pos
            || pos == rhs.pos && act < rhs.act;
    }
};

int main() {
    LL tt;
    cin >> tt;
    for (LL t = 1; t <= tt; ++t) {
        cin >> n >> m;
        LL cost = 0;
        vector<Event> events;
        for (LL i = 0; i < m; ++i) {
            LL b, e;
            LL p;
            cin >> b >> e >> p;
            Event evt(b, 0, p);
            events.push_back(evt);
            evt = Event(e, 1, p);
            events.push_back(evt);
            cost = (cost + p * (Cost(e - b) % MOD)) % MOD;
        }

        sort(events.begin(), events.end());

        LL min_cost = 0;

        stack< pair<LL, LL> > s;
        for (LL i = 0; i < events.size(); ++i) {
            const Event& evt = events[i];
            if (evt.act == 0) {
                s.push(make_pair(evt.pos, evt.cnt));
                continue;
            }
            LL left = evt.cnt;
            while (left) {
                pair<LL, LL> p = s.top(); s.pop();
                LL drop = min(p.second, left); left -= drop;
                min_cost = (min_cost + drop * (Cost(evt.pos - p.first) % MOD)) % MOD;
                if (drop < p.second) {
                    p.second -= drop;
                    s.push(p);
                }
            }
        }
        cerr << cost << ' ' << min_cost << '\n';
        LL ans = (cost + MOD - min_cost) % MOD;

        cout << "Case #" << t << ": " << ans << '\n';
    }

    return 0;
}

