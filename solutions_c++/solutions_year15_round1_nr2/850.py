#include<bits/stdc++.h>
#define sc scanf
#define pr printf
#define fr first
#define se second
#define pb push_back
#define mp make_pair
using namespace std;
const int MN = 5010;
const long long INF = (1LL<<30);
const int MOD = (1e+9) + 7;
int B, N, m[MN];
int main(){
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    int t;
    sc("%d", &t);
    for (int k = 1; k <= t; k++) {
        sc("%d%d", &B, &N);
        for (int i = 0; i < B; i++) {
            sc("%d", &m[i]);
        }
        for (int i = 0; i < B; i++) {
            long long L = 1LL, R = INF, M, num;
            while (L < R) {
                M = (L + R) / 2;
                num = M;
                for (int j = 0; j < i; j++) {
                    num += (M - 1) * m[i] / m[j] + 1LL;
                }
                for (int j = i + 1; j < B; j++) {
                    num += ((M - 1) * m[i] + m[j] - 1LL) / m[j];
                }
                if (num >= N) {
                    R = M;
                }
                else {
                    L = M + 1;
                }
            }
            //pr("%d %lld\n", i, R);
            num = R;
            for (int j = 0; j < i; j++) {
                num += (R - 1) * m[i] / m[j] + 1;
            }
            for (int j = i + 1; j < B; j++) {
                num += ((R - 1) * m[i] + m[j] - 1) / m[j];
            }
            if(num == N) {
                pr("Case #%d: %d\n", k, i + 1);
                break;
            }
        }
    }
    return 0;
}

