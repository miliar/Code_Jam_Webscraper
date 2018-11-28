#include <stdio.h>
#include <vector>
#include <string.h>
#include <algorithm>

using namespace std;

#define MOD 1000000007
#define INF 0x3f3f3f3f
#define MAX 1005

typedef long long LL;

double A[MAX];
double B[MAX];

int main(void) {
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D.out", "w", stdout);
    int nCase;
    while (~scanf("%d", &nCase)) {
        for (int cas = 1; cas <= nCase; ++cas) {    
            int N;
            scanf("%d", &N);
            for (int i = 0; i < N; ++i) {
                scanf("%lf", &A[i]);
            }
            for (int i = 0; i < N; ++i) {
                scanf("%lf", &B[i]);
            }
            sort(A, A + N);
            sort(B, B + N);

            int nSumA = 0;
            int S = 0;
            int nSumB = 0;
            for (int i = 0; i < N; ++i) {
                nSumA += (A[i] > B[i]);
            }
            for (int i = 0; i < N; ++i) {
                if (A[i] > B[N - 1 - i]) {
                    ++S;
                }
                int temp = 0;
                for (int k = 0, j = N - 1 - i - 1; j >= 0; ++k, --j) {
                    temp += (A[N - 1 - k] > B[j] ? 1 : 0);
                }
                nSumA = max(nSumA, S + temp);
            }
            
            bool vis[MAX];
            memset(vis, false, sizeof(vis));
            for (int i = 0; i < N; ++i) {
                int j;
                for (j = 0; j < N; ++j) {
                    if (vis[j]) {
                        continue;
                    }
                    if (B[j] > A[i]) {
                        vis[j] = true;
                        break;
                    }
                }
                if (j >= N) {
                    ++nSumB;
                }
            }

            printf("Case #%d: %d %d\n", cas, nSumA, nSumB);
        }
    }
    return 0;
}