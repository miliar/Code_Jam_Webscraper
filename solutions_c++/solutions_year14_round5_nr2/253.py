#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <map>
#include <set>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

#define forn(i, n) for (int i = 0; i < (n); ++i)
typedef pair<int, int> ii;
typedef vector<ii> vii;

int P, Q, n;

map<pair<vii, int>, int> cache;

int go(vii v, int turn) {
    if (v.empty()) return 0;
    
    auto z = make_pair(v, turn);
    auto saved = cache.find(z);
    if (saved != cache.end()) return saved->second;

    if (turn == 2) {
        vii w = v;
        w[0].first -= Q;
        if (w[0].first <= 0) {
            w.erase(w.begin());
        }
        return cache[z] = go(w, 3 - turn);
    }

    vii w = v;
    int ans = go(w, 3 - turn);

    forn(i, (int) v.size()) {
        w = v;
        int cur = 0;
        w[i].first -= P;
        if (w[i].first <= 0) {
            cur += w[i].second;
            w.erase(w.begin() + i);
        }
        cur += go(w, 3 - turn);
        ans = max(ans, cur);
    }

    return cache[z] = ans;
}

int main() {
    int __;
    scanf("%d", &__);
    forn(_, __) {
        cache.clear();
        scanf("%d%d%d", &P, &Q, &n);
        vii v;
        forn(i, n) {
            int h, g;
            scanf("%d%d", &h, &g);
            v.push_back(ii(h, g));
        }
        // forn(i, n) printf("%d %d\n", v[i].first, v[i].second);
        printf("Case #%d: %d\n", _+1, go(v, 1));
        fprintf(stderr, " %d", _+1);
    }
    fprintf(stderr, "\n");
    return 0;
}
