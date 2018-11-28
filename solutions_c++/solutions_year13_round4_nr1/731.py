#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;

typedef long long lint;

const lint MOD = 1000002013;

struct rec_t {
    lint o, p;
    bool operator<(const rec_t &another) const {
        return o < another.o;
    }
};

int N, M;

bool cmp(const rec_t &a, const rec_t &b) {
    return a.o < b.o; }

lint getGain(lint o, lint e, lint p) {
    lint dis = e - o;
    lint res = dis;
    res = res * (N + N - dis + 1) / 2;
    res %= MOD;
    res *= p % MOD;
    res %= MOD;
//    cout << o << "-->" << e << " " << p << "===" << res << endl;//
    return res;
}
    
int main(int argc, char *argv[]) {
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        scanf("%d %d", &N, &M);
        rec_t in[M];
        rec_t out[M];
        lint gain1 = 0, gain2 = 0;
        for (int ix = 0; ix < M; ++ix) {
            lint o, e, p;
            scanf("%lld %lld %lld", &o, &e, &p);
            //cin >> o >> e >> p;
            in[ix].o = o, in[ix].p = p;
            out[ix].o = e, out[ix].p = p;
            gain1 += getGain(o, e, p);
            gain1 %= MOD;
        }
        sort(in, in+M, cmp);
        sort(out, out+M, cmp);
//        cout << "::::" << in[0].o << endl;//
        
        int now = 0, cur = 0;
        for (int ix = 0; ix < M; ++ix) {
            while (cur < M && in[cur].o <= out[ix].o) {
                if (in[cur].o == in[now].o) {
                    in[now].p += in[cur].p;
                }
                else {
                    in[++now].o = in[cur].o;
                    in[now].p = in[cur].p;
                }
                ++cur;
            }
//            cout << ix << ": " << now << " " << cur << endl;//
            while (out[ix].p > 0) {
                if (in[now].p < out[ix].p) {//FIXME: ==
                    out[ix].p -= in[now].p;
                    gain2 += getGain(in[now].o, out[ix].o, in[now].p);
                    in[now].p = 0;
                    --now;
                }
                else {
                    in[now].p -= out[ix].p;
                    gain2 += getGain(in[now].o, out[ix].o, out[ix].p);
                    out[ix].p = 0;
                }
                gain2 %= MOD;
//                cout << "contin " << out[ix].p << " " << now << " " << endl;//
            }
//            cout << now << " " << in[now].o << " " << in[now].p << endl;
        }
//        cout << gain1 << " " << gain2 << endl;///
        
        lint ans = (gain1 + MOD - gain2) % MOD;
        printf("Case #%d: %lld\n", ca, ans);
    }
    return 0;
}

