#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;
const int MAXN = 110;
int in[MAXN][MAXN];
int rmax[MAXN], rmin[MAXN];
int cmax[MAXN], cmin[MAXN];
int T, N, M;

int main()
{
    freopen("B-small-attempt2.in", "r", stdin);
    freopen("test.out", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%d%d", &N, &M);
        memset(rmax, -1, sizeof(rmax));
        memset(cmax, -1, sizeof(cmax));
        memset(rmin, 0x3f, sizeof(rmin));
        memset(cmin, 0x3f, sizeof(cmin));
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                scanf("%d", &in[i][j]);
                rmax[i] = max(rmax[i], in[i][j]);
                rmin[i] = min(rmin[i], in[i][j]);
                cmax[j] = max(cmax[j], in[i][j]);
                cmin[j] = min(cmin[j], in[i][j]);
            }
        }
        //cout << N <<' '<<M<<endl;
        bool flag = true;
        if (N != 1 && M != 1) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    //printf("in[%d][%d] = %d, rmax[%d] = %d, rmin[%d] = %d, cmax[%d] = %d, cmin[%d] = %d\n", i, j, in[i][j], i, rmax[i], i, rmin[i], j, cmax[j], j, cmin[j]);
                    if (rmax[i] != rmin[i] && cmax[j] != cmin[j]) {
                        if (rmin[i] == in[i][j] && in[i][j] == cmin[j]) {
                            flag = false;
                            break;
                        }
                    }
                }
                if (!flag)  break;
            }
        }
        if (flag)   printf("Case #%d: YES\n", cas);
        else        printf("Case #%d: NO\n", cas);
    }
    return 0;
}
