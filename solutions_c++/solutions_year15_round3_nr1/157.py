
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

int main(void) {
    int T, cas = 1;
    scanf("%d", &T);
    while (T-- > 0) {
        int r, c, w;
        scanf("%d %d %d", &r, &c, &w);
        int ans = (c / w) * r;
        if (c % w == 0) --ans;
        ans += w ;
        printf("Case #%d: %d\n", cas++, ans);
    }

    return 0;
}
