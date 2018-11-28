#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

const int N = 2000010;

struct bis {
    int maxIndex;
    vector<long long> tree;

    bis(int mIndex)
        : maxIndex(mIndex)
        , tree(mIndex, 0) {}

    void update(int index, int delta) {
        for (; index <= maxIndex; index += last(index))
            tree[index] += delta;
    }

    long long prefixSum(int index) {
        long long ans = 0;
        for (; index > 0; index -= last(index))
            ans += tree[index];
        return ans;
    }

    int last(int x) {
        return x & (-x);
    }
};

struct point {
    long long x;
    long long y;
    bool p;

    int ans_id;
    int sign;

    point(long long xx, long long yy)
        : x(xx), y(yy), p(true) {}
    point(long long xx, long long yy, int aid, int asign)
        : x(xx), y(yy), p(false), ans_id(aid), sign(asign) {}

    bool operator<(const point& r) const {
        if (x != r.x)
            return x < r.x;
        if (y != r.y)
            return y < r.y;
        if (p != r.p)
            return p;
        return false;
    }
};

int main() {
    int T;
    cin >> T;
    for (int ncase = 1; ncase <= T; ++ncase) {
        int n;
        long long d;
        cin >> n >> d;
        vector<long long> s(n), m(n);
        long long as, cs, rs, am, cm, rm;
        cin >> s[0] >> as >> cs >> rs
            >> m[0] >> am >> cm >> rm;
        for (int i = 0; i + 1 < n; ++i) {
            s[i + 1] = (s[i] * as + cs) % rs;
            m[i + 1] = (m[i] * am + cm) % rm;
        }
        for (int i = 1; i < n; ++i)
            m[i] %= i;

        vector<point> nodes;

        vector< pair<long long, long long> > salary_range(n);
        for (int i = 0; i < n; ++i) {
            if (i == 0) {
                salary_range[0].first = s[0];
                salary_range[0].second = s[0];
            } else {
                salary_range[i].first = min(salary_range[m[i]].first, s[i]);
                salary_range[i].second = max(salary_range[m[i]].second, s[i]);
            }
            nodes.push_back(point(salary_range[i].first, salary_range[i].second));
        }
        vector<long long> ans(n, 0);
        for (int i = 0; i < n; ++i) {
            // [ s[i], s[i] + d ]
            nodes.push_back(point(s[i] + d, s[i] + d, i, 1));
            nodes.push_back(point(s[i] - 1, s[i] - 1, i, 1));
            nodes.push_back(point(s[i] - 1, s[i] + d, i, -1));
            nodes.push_back(point(s[i] + d, s[i] - 1, i, -1));
        }

        sort(nodes.begin(), nodes.end());

        bis tree(N);
        for (int i = 0; i < (int) nodes.size(); ++i) {
            if (nodes[i].p)
                tree.update(nodes[i].y, 1);
            else
                ans[nodes[i].ans_id] += nodes[i].sign * tree.prefixSum(nodes[i].y);
        }

        long long best = 0;
        for (int i = 0; i < n; ++i)
            best = max(best, ans[i]);

        cout << "Case #" << ncase << ": " << best << endl;
    }
    return 0;
}
