#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<algorithm>
using namespace std;

struct event {
    int d, w, l, s;
    event(int _d, int _w, int _l, int _s): d(_d), w(_w), l(_l), s(_s){}
    bool operator<(const event& e) const {
        return this->d < e.d;
    }
};

int T;
int D, N, W, E, S, DD, DP, DS;
int n;
int b[601];
const int tt = 300;

int check(const event& e) {
    int p = e.w + e.l;
    int s = e.s;
    for (int i = e.w; i < p; ++i) {
        if (b[i] < e.s) {
            return 1;
        }
    }
    return 0;
}

void maintain(const event& e) {
    int p = e.w + e.l;
    int s = e.s;
    for (int i = e.w; i < p; ++i) {
        if (b[i] < e.s) {
            b[i] = e.s;
        }
    }
}

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small.out", "w", stdout);
    scanf("%d", &T);
    for (int test = 1; test <= T; ++test) {
        vector<event> v;
        scanf("%d", &n);
        memset(b, 0, sizeof(b));
        for (int i = 0 ; i < n; ++i) {
            scanf("%d%d%d%d%d%d%d%d", &D, &N, &W, &E, &S, &DD, &DP, &DS);
            int l = E - W;
            W += tt;
            for (int j = 0; j < N; ++j) {
                v.push_back(event(D, W, l, S));
                D += DD;
                W += DP;
                S += DS;
            }
        }
        sort(v.begin(), v.end());
        int sz = v.size();
        int now = 0;
        int ans = 0;
        for (int i = 1; i <= sz; ++i) {
            if (i == sz || v[i].d != v[i - 1] .d) {
                for (int j = now; j < i; ++j) {
                    ans += check(v[j]);
                }
                for (int j = now; j < i; ++j) {
                    maintain(v[j]);
                }
                now = i;
            }
        }
        printf("Case #%d: %d\n", test, ans);
    }
    return 0;
}

