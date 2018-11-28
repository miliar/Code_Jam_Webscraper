#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <queue>
#include <stack>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

long long fee(int N, int o, int e) {
    long long k = e - o;
    return k * N - k * (k - 1) / 2;
}
int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        int N, M;
        scanf("%d%d", &N, &M);
        map<int, pair<int, int> > m;
        long long orig = 0;
        for (int i = 0; i < M; ++i) {
            int o, e, p; 
            scanf("%d%d%d", &o, &e, &p);
            m[o].first += p;
            m[e].second += p;
            orig += p * fee(N, o, e);
        }
        long long cost = 0;
        stack<pair<int, int> > st;
        map<int, pair<int, int> >::iterator it = m.begin();
        while (it != m.end()) {
            int pos = it->first;
            pair<int, int>& p = it->second;
            int o = p.first;
            int e = p.second;
            //printf("pos: %d, o:%d, e:%d\n", pos, o, e);
            if (o > e) {
                o = o - e;
                st.push(make_pair(pos, o));
            } else if (o < e) {
                e = e - o;
                while (e > 0) {
                    pair<int, int>& oo = st.top();
                    int ne = 0;
                    if (oo.second >= e) {
                        oo.second -= e;
                        ne = e;
                    } else {
                        ne = oo.second;
                        oo.second = 0;
                    }
                    //printf("ne: %d\n", ne);
                    cost += ne * fee(N, oo.first, pos);
                    e -= ne;
                    //printf("oo.second: %d, cost: %lld\n", oo.second, cost);
                    if (oo.second == 0) {
                        st.pop();
                    }
                }
            } else {
            }
            it++;
        }
        printf("Case #%d: %lld\n", t, orig - cost);
    }
    return 0;
}
