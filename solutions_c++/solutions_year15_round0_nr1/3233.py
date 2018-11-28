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
    freopen("F:\\retired\\gcj2015\\A-large.in","r",stdin);
    freopen("F:\\retired\\gcj2015\\out.txt","w",stdout);
    int cas;
    int n;
    int cnt, inv;
    char shy[MAXN];
    scanf("%d", &cas);
    for (int ca = 1; ca <= cas; ++ca) {
        scanf("%d%s", &n, shy);
        cnt = inv = 0;
        for (int i = 0; i <= n; ++i) {
            if (cnt < i) {
                inv += i - cnt;
                cnt = i;
            }
            cnt += shy[i] - '0';
        }
        printf("Case #%d: %d\n", ca, inv);
    }
    return 0;
}
