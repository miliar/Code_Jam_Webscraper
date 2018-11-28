#include <bits/stdc++.h>

using namespace std;

vector<int> pancakes;

int main() {
    int T, t, D, d, v, maxv, maxh, tans, ans;
    scanf("%d", &T);
    for(t = 0; t < T; ++t) {
        scanf("%d", &D);
        ans = 1000;
        pancakes.clear();
        maxv = 0;
        for(d = 0; d < D; ++d) {
            scanf("%d", &v);
            pancakes.push_back(v);
            maxv = max(maxv, v);
        }
        sort(pancakes.begin(), pancakes.end());
        for(maxh = 1; maxh <= maxv; ++maxh) {
            tans = 0;
            for(d = D-1; d >= 0; --d) {
                if(pancakes[d] <= maxh) {
                    break;
                } else {
                    tans += ceil(pancakes[d] / (double) maxh)-1;
                }
            }
            ans = min(ans, tans + maxh);
        }
        printf("Case #%d: %d\n", t+1, ans);
    }
    return 0;
}
