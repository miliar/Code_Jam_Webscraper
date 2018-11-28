#include <iostream>
#include <set>
#include <algorithm>
#include <vector>
#include <limits>
#include <queue>

using namespace std;

const long long MAXN = 1000;
const long long INF = numeric_limits<long long>::max();

long long pdist(long long x1, long long y1, long long x2, long long y2) {
    return max(abs(x1 - x2), abs(y1 - y2));
}

struct rect {
    long long x[2];
    long long y[2];
};

long long prdist(long long x, long long y, rect r) {
    if (!((r.x[0] < x && x < r.x[1]) || (r.y[0] < y && y < r.y[1]))) {
        long long d = INF;
        for (long long i = 0; i < 2; i++)
            for (long long j = 0; j < 2; j++)
                d = min(d, pdist(x, y, r.x[i], r.y[j]));
        return d;
    } else if (r.x[0] <= x && x <= r.x[1]) {
        return min(abs(r.y[0] - y), abs(r.y[1] - y));
    } else {
        return min(abs(r.x[0] - x), abs(r.x[1] - x));
    }
}

long long rdist(rect a, rect b) {
    long long d = INF;

    for (long long i = 0; i < 2; i++)
        for (long long j = 0; j < 2; j++) {
            d = min(d, prdist(a.x[i], a.y[j], b) - 1);
            d = min(d, prdist(b.x[i], b.y[j], a) - 1);
        }

    return d;
}

long long dijkstra(vector<vector<pair<long long, long long> > > &g, long long origin, long long dest) {
    set<pair<long long, long long> > q;
    q.insert(make_pair(0, origin));
    vector<long long> cost(g.size(), INF);
    cost[origin] = 0;

    while (!q.empty()) {
        auto next = *q.begin();
        q.erase(q.begin());

        long long v = next.second;

        if (v == dest)
            return cost[dest];

        if (next.first > cost[v])
            continue;

        for (long long i = 0; i < g[v].size(); i++) {
            if (cost[g[v][i].first] > cost[v] + g[v][i].second) {
                cost[g[v][i].first] = cost[v] + g[v][i].second;
                q.insert(make_pair(cost[g[v][i].first], g[v][i].first));
            }
        }
    }

    return INF;
}

int main() {
    long long t;
    cin >> t;

    for (long long tc = 1; tc <= t; tc++) {
        long long w, h, b;
        cin >> w >> h >> b;

        vector<rect> bs(b);

        for (long long i = 0; i < b; i++) {
            cin >> bs[i].x[0] >> bs[i].y[0] >> bs[i].x[1] >> bs[i].y[1];
        }

        vector<vector<pair<long long, long long> > > g(b + 2);

        for (long long i = 0; i < b; i++) {
            for (long long j = 0; j < b; j++) {
                if (i != j) {
                    g[i].push_back(make_pair(j, rdist(bs[i], bs[j])));
//                    cerr << "Dist between rectangles " << i << " and " << j << ": " << rdist(bs[i], bs[j]) << endl;
                }
            }

            g[b].push_back(make_pair(i, bs[i].x[0]));
            g[i].push_back(make_pair(b + 1, w - bs[i].x[1] - 1));
        }

        g[b].push_back(make_pair(b+1, w));

        cout << "Case #" << tc << ": " << dijkstra(g, b, b + 1) << '\n';
    }

    return 0;
}
