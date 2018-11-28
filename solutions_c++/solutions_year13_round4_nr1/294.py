#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <stack>
#define OUT(x) cerr << #x << ": " << (x) << endl
#define SZ(x) ((int)x.size())
#define FOR(i, n) for (int i = 0; i < (n); ++i)
using namespace std;
typedef long long LL;

int T, N, M;
typedef pair<int, int> PII;
vector<PII> pnt;
const int MOD = 1000002013;

LL gao(LL N, int k) {
    LL ans = (N + (N - k + 1)) * k / 2;
    return ans % MOD;
}

int main() {
    scanf("%d", &T);
    for (int id = 1; id <= T; ++id) {
        scanf("%d%d", &N, &M);
        pnt.clear();
        LL orig = 0;
        FOR(i, M) {
            int a, b, c;
            scanf("%d%d%d", &a, &b, &c);
            pnt.push_back(PII(a, -c)); // enter
            pnt.push_back(PII(b, +c)); // leave
            orig = (orig + gao(N, b - a) * c % MOD) % MOD;
        }
        sort(pnt.begin(), pnt.end());
        stack<PII> st;
        LL ans = 0;
        for (int i = 0; i < SZ(pnt); ++i) {
            if (pnt[i].second < 0) {
                st.push(PII(pnt[i].first, -pnt[i].second));
            } else {
                int cnt = pnt[i].second;
                while (cnt > 0) {
                    int pos = st.top().first, need = min(st.top().second, cnt);
                    cnt -= need;
                    st.top().second -= need;
                    ans = (ans + (LL)gao(N, pnt[i].first - pos) * need % MOD) % MOD;
                    if (st.top().second == 0) st.pop();
                }
            }
        }
        //OUT(orig), OUT(ans);
        LL ans2 = orig - ans;
        ans2 = (ans2 % MOD + MOD) % MOD;
        cout << "Case #" << id << ": " << ans2 << endl;
    }
    return 0;
}
