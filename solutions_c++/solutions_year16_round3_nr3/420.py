#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

struct triplet {
    int a, b, c;
} v[1024];

int M1[8][8], M2[8][8], M3[8][8];

int main() {

    freopen("C-small-attempt2.in", "r", stdin);
    freopen("C-small-attempt2.out", "w", stdout);

    int T; scanf("%d", &T);

    for(int ncase=1; ncase<=T; ncase++) {
        int J, P, S, K;
        scanf("%d%d%d%d", &J, &P, &S, &K);

        int idx = 0;
        for(int i=0; i<J; i++) {
            for(int j=0; j<P; j++) {
                for(int k=0; k<S; k++) {
                    v[idx].a = i;
                    v[idx].b = j;
                    v[idx].c = k;
                    idx++;
                }
            }
        }

        int ans = -1;
        int best = -1;
        for(int mask=(1<<idx)-1; mask>=0; mask--) {
            if (__builtin_popcount(mask) < best) continue;
            int days = 0;
            memset(M1, 0, sizeof(M1));
            memset(M2, 0, sizeof(M2));
            memset(M3, 0, sizeof(M3));
            for(int i=0; i<idx; i++) {
                if (((1<<i) & mask) == 0) continue;
                days++;
                M1[ v[i].a ][ v[i].b ]++;
                M2[ v[i].b ][ v[i].c ]++;
                M3[ v[i].a ][ v[i].c ]++;
                if (M1[ v[i].a ][ v[i].b ] > K) {
                    days = -1;
                    break;
                }
                if (M2[ v[i].b ][ v[i].c ] > K) {
                    days = -1;
                    break;
                }
                if (M3[ v[i].a ][ v[i].c ] > K) {
                    days = -1;
                    break;
                }
            }
            if (days > best) {
                ans = mask;
                best = days;
            }
        }

        printf("Case #%d: %d\n", ncase, __builtin_popcount(ans));
        for(int i=0; i<idx; i++) {
            if ((1<<i)&ans) {
                printf("%d %d %d\n", v[i].a+1, v[i].b+1, v[i].c+1);
            }
        }
    }

    return 0;
}
