#include <iostream>
#include <cstdio>
#include <set>
#include <vector>
#include <cassert>

using namespace std;

typedef long long int LL;

#define FI first
#define SE second
#define MP make_pair
#define PB push_back

struct triple {
    int tm, tp;
    LL pp;
    triple(int _tm, int _tp, LL _pp) : tm(_tm), tp(_tp), pp(_pp) {}
};

struct cmp {
    bool operator()(const triple& a, const triple& b) {
        if (a.tm == b.tm)
            return a.tp < b.tp;
        return a.tm < b.tm;
    }
};

multiset< pair<int, int> > in;
multiset<triple, cmp> events;

LL count(int n, int o, int e) {
    if (o != e)
        return LL(2 * n - (e - o - 1)) * (e - o) / 2;
    else
        return 0;
}

int main() {

    int t, n, m, o, i, e, p;
    LL res_h, res_c;

    scanf("%d", &t);

    for (int i = 1; i <= t; ++i) {

        scanf("%d %d", &n, &m);
        res_h = res_c = 0;

        for (int j = 0; j < m; ++j) {
            scanf("%d %d %d", &o, &e, &p);
            events.insert(triple(o, 0, p));
            events.insert(triple(e, 1, p));
            res_h += count(n, o, e) * LL(p);
        }

        for (auto it = events.begin(); it != events.end(); ++it) {
            if (it->tp == 0) {
                // printf("na %d wsiada %d\n", it->tm, it->pp);
                in.insert(MP(it->tm, it->pp));
            } else {
                int left = it->pp;
                // printf("na %d wysiada:\n", it->tm);
                while (left) {
                    assert(in.size());
                    pair<int, int> last = *(--in.end());
                    in.erase(--in.end());
                    int out = min(left, last.SE);
                    // printf("out %d, left %d, last %d\n", out, left, last.SE);
                    // printf("\t%d z %d\n", out, last.FI);
                    res_c += count(n, last.FI, it->tm) * LL(out);
                    left -= out;
                    if (left == 0 && last.SE > out)
                        in.insert(MP(last.FI, last.SE - out));
                }
            }
        }

        events.clear();
        in.clear();

        printf("Case #%d: %lld\n", i, res_h - res_c);
    }

    return 0;
}

