#include<set>
#include<map>
#include<cmath>
#include<queue>
#include<cstdio>
#include<vector>
#include<string>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

#define mem(a, b) (memset(a, b, sizeof(a)))
#define pb push_back
#define all(v) v.begin(), v.end()
#define rall(v) v.rbegin(), v.rend()
#define rep(i, m) for (int i = 0; i < (int)(m); i++)
#define rep2(i, n, m) for (int i = n; i < (int)(m); i++)
typedef long long LL;
typedef pair<int, int> pii;

const int oo = (int) 1e9;
const double PI = 2 * acos(0);
const double eps = 1e-9;

int p[1010];



int main(void) {
    int T, cas = 1;
    scanf("%d", &T);
    while (T--) {
        int D;
        scanf("%d", &D);
        int tmp = 0;
        for (int i = 0; i < D; i++) {
            scanf("%d", p+i);
            tmp = max(tmp, p[i]);
        }
        int ans = oo;
        for (int i = 1; i <= tmp; i++) {
            int cc = 0;
            for (int j = 0; j < D; j++) if (p[j] > i) {
                cc += p[j] / i;
                if (p[j] % i) ++cc;
                --cc;
            }
            ans = min(ans, i+cc);
        }

        printf("Case #%d: %d\n", cas++, ans);
    }

    return 0;
}
