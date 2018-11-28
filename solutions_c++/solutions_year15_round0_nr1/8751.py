#include <iostream>
#include <cstdio>
using namespace std;
typedef long long int LL;
char line[1111];
int N;
LL ans, ccount;
void solve(int cs) {
    ans = 0;
    ccount = 0;
    scanf("%d %s\n", &N, line);
    for (int i = 0; i <= N; i++) {
        if (line[i] != '0') {
            if (ccount < i) {
                ans = ans + (i - ccount);
                ccount += (i - ccount + line[i] - '0');
            } else {
                ccount = ccount + (line[i] - '0');
            }
        }
    }
    printf("Case #%d: %lld\n", cs, ans);
}
int main() {
#ifdef LOCAL
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
#endif
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        solve(i);
    }
    return 0;
}

