#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <numeric>
#include <algorithm>
#include <bitset>
#include <complex>

using namespace std;

typedef unsigned uint;
typedef long long Int;

const int INF = 1001001001;
const Int INFLL = 1001001001001001001LL;

template<typename T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i << " "; cout << endl; }
template<typename T> void chmin(T& a, T b) { if (a > b) a = b; }
template<typename T> void chmax(T& a, T b) { if (a < b) a = b; }

const Int MO = 1000002013;

struct event {
    int pos, cnt;
    enum typ_t { IN, OUT } typ;
    event(int p, int c, typ_t t) : pos(p), cnt(c), typ(t) { }
};
bool operator < (const event& e, const event& f)
{
    if (e.pos != f.pos) return e.pos < f.pos;
    return e.typ == event::IN && f.typ == event::OUT;
}

int main()
{
    int T;
    cin >> T;

    for (int CN = 1; CN <= T; ++CN) {
        int N, M;
        cin >> N >> M;

        Int ord = 0;
    
        vector<event> es;
        for (int i = 0; i < M; ++i) {
            int o, e, p;
            cin >> o >> e >> p;
            es.push_back(event(o, p, event::IN));
            es.push_back(event(e, p, event::OUT));
            ord += (Int)(e - o) * (e - o - 1) / 2 % MO * p % MO;
            ord %= MO;
        }
        sort(es.begin(), es.end());

        Int maxi = 0;
        priority_queue<pair<Int, Int> > qs;
        for (int i = 0; i < es.size(); ++i) {
            if (es[i].typ == event::IN) {
                qs.push(make_pair(es[i].pos, es[i].cnt));
            } else {
                Int cc = es[i].cnt;
                while (cc > 0) {
                    pair<Int, Int> t = qs.top(); qs.pop();
                    Int u = min(cc, t.second);
                    maxi += (Int)(es[i].pos - t.first) * (es[i].pos - t.first - 1) / 2 % MO * u % MO;
                    maxi %= MO;
                    if (t.second != u) {
                        t.second -= u;
                        qs.push(t);
                    }
                    cc -= u;
                }
            }
        }

        cout << "Case #" << CN << ": " << (maxi - ord + MO) % MO << endl;
    }

    return 0;
}
