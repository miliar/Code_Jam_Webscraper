#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;

const int MOD = 1000002013;
typedef pair<int, int> PII;

int T;
int n, m;
int x, y, z;

long long calc(int x, int y, int z) {
    long long N = y - x;
    return (n + n - N + 1) * N / 2 % MOD * z % MOD;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &T);
    for (int test = 1; test <= T; ++test) {
        long long ans = 0;
        vector<PII> u, v;
        scanf("%d%d", &n, &m);
        for (int i = 0; i < m; ++i) {
            scanf("%d%d%d", &x, &y, &z);
            v.push_back(make_pair(x, z));
            u.push_back(make_pair(y, z));
            ans += calc(x, y, z); 
            ans %= MOD;
        }
        sort(v.begin(), v.end());
        sort(u.begin(), u.end());
        for (int i = 0; i < m; ++i) {
            vector<PII>::iterator p = upper_bound(v.begin(), v.end(), make_pair(u[i].first, MOD));
            --p;
            int t = u[i].second;
            while (t) {
                if (t > p->second) {
                    t-= p->second;
                    ans -= calc(p->first, u[i].first, p->second);
                    p->second = 0;
                    --p;
                } else {
                    p->second -= t;
                    ans -= calc(p->first, u[i].first, t);
                    ans %= MOD;
                    break;
                }
            }
        }
        printf("Case #%d: %I64d\n", test, (ans + MOD) % MOD);
    }
    return 0;
}

