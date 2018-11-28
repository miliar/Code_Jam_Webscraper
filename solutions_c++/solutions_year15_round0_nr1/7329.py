#include <bits/stdc++.h>
using namespace std;

int T, N, S[1050], caseNo = 1;
char buf[1050];

int main() {
    scanf("%d", &T);
    while(T--) {
        scanf("%d %s", &N, buf);
        N++;
        for(int i = 0; i < N; i++) {
            S[i] = buf[i] - '0';
        }
        int sum = 0, ans = 0;
        for(int i = 0; i < N; i++) {
            if (sum < i) {
                ans += i - sum;
                sum = i;
            }
            sum += S[i];
        }
        printf("Case #%d: %d\n", caseNo++, ans);
    }
    return 0;
}
