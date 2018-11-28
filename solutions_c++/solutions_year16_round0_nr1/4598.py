#include <iostream>
#include <stdio.h>
#include <algorithm>
typedef long long ll;
using namespace std;
int tt;
ll get(ll N) {
    if(N == 0) return -1;
    ll h = 0; ll target = (1LL << 10) - 1, ans;
    for(int i = 1; h != target; i++) {
        ll curr = i * N; ans = curr;
        while(curr > 0) {
            int digit = curr % 10; h |= (1LL << digit);
            curr /= 10;
        }
    }
    return ans;
}
void solve() {
    ll N; scanf("%lld", &N);
    ll ans = get(N);
    printf("Case #%d: ", tt);
    if(ans <= 0) printf("INSOMNIA\n");
    else printf("%lld\n", ans);
}
int main() {
    int t = 1; scanf("%d", &t);
    for(tt = 1; tt <= t; tt++) solve();
}
