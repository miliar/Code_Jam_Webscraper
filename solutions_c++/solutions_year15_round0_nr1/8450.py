#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <queue>
#include <map>
#include <string>
#include <stack>
#include <bitset>
#include <vector>

using namespace std;
char s[1100];
int main() {
    #ifdef LOCAL
    freopen("A-large.in", "r", stdin);
    freopen("out2.txt", "w", stdout);
    #endif
    int T, cas = 1;
    scanf("%d", &T);
    while(T--) {
        int n;
        scanf("%d%s", &n, s);
        int sum = 0;
        long long ans = 0;
        for(int i = 0; i < n + 1; i++) {
            int t = s[i] - '0';
            if(t) {
                if(sum < i) ans += i - sum, sum += i - sum;
                sum += t;
            }
        }
        printf("Case #%d: %lld\n", cas++, ans);
    }
    return 0;
}
