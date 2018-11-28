
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
typedef pair<int, int> PII;
typedef pair<LL, LL> PLL;

const int oo = (int) 1e9;
const double eps = 1e-9;

int d[110];
set<int>  s;
int main(void) {
    int T, cas = 1;
    scanf("%d", &T);
    while (T-- > 0) {
        printf("Case #%d: ", cas++);
        int C, D, V;
        scanf("%d %d %d", &C, &D, &V);
        s.clear();
        for (int i = 0; i < D; ++i) {
            scanf("%d", d + i);
            s.insert(d[i]);
        }
        sort(d, d + D);
        int ans = 0;
        LL A = 1;
        int i = 0;
        while (A <= V) {
            LL a = A;
            if (s.find(A) == s.end()) {
                ++ans;
            }
            A = C * A + A;
            while (i < D && d[i] < A) {
                if (d[i] != a)
                    A += (LL)C * d[i];
                ++i;
            }
        }
        printf("%d\n", ans);

    }

    return 0;
}
