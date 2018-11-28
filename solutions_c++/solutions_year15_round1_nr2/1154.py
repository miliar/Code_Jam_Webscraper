#include <bits/stdc++.h>
using namespace std;

int main() {
    int T, N, B, M[1001];

    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d %d", &B, &N);
        for (int i = 1; i <= B; i++)
            scanf("%d", &M[i]);

        int ans = 0;
        long long lo = 1, hi = 1LL<<60;
        do {
            long long mid = (lo + hi)/2;
            long long sum = 0, b = 0;
            vector<int> id;
            for (int i = 1; i <= B; i++) {
                sum += (mid + M[i] - 1) / M[i];
                if (mid % M[i] == 0) {
                    b++;
                    id.push_back(i);
                }
            }

            if (sum + b < N) {
                lo = mid+1;
            } else {
                hi = mid;
                if (sum < N && b) {
                    ans = id[N-sum-1];
                } else if (b >= N) {
                    ans = id[N-1];
                }
            }
        } while (lo < hi);
        printf("Case #%d: %d\n", t, ans);
    }
}
