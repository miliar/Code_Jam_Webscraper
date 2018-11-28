#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <queue>
#include <map>
#define FI first
#define SE second
using namespace std;
const double EPS = 1e-8;
const int MAXN = 1005;
const int INF = 1111111111;
int main() {
    freopen("F:\\retired\\gcj2015\\B-large.in","r",stdin);
    //freopen("F:\\retired\\gcj2015\\in.txt","r",stdin);
    freopen("F:\\retired\\gcj2015\\out.txt","w",stdout);
    int cas;
    int n;
    int tmp, ans, mv;
    int pan[MAXN];
    scanf("%d", &cas);
    for (int ca = 1; ca <= cas; ++ca) {
        scanf("%d", &n);
        ans = 0;
        for (int i = 0 ; i < n; ++i) {
            scanf("%d", &pan[i]);
            ans = max(ans, pan[i]);
        }
        for (int i = 2; i < ans; ++i) {
            mv = 0;
            for (int j = 0; j < n; ++j) {
                mv += pan[j] / i - (pan[j] % i == 0);
            }
            ans = min(ans, mv + i);
        }
        printf("Case #%d: %d\n", ca, ans);
    }
    return 0;
}
