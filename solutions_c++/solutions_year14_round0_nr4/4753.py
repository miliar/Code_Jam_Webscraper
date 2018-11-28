#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;

const int maxn = 1000;
const double eps = 1e-6;

double nao[maxn], ken[maxn];
bool ken_vis[maxn];

int dcmp(double x) {
    if(fabs(x) < eps) return 0;
    return x > 0 ? 1 : -1;
}

int main()
{
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    int T, N, kase = 0;
    scanf("%d", &T);
    while(T--) {
        scanf("%d", &N);
        for(int i = 0; i < N; i++) scanf("%lf", nao+i);
        for(int i = 0; i < N; i++) scanf("%lf", ken+i);
        sort(nao, nao + N);
        sort(ken, ken + N);
        int scores_1 = 0;
        memset(ken_vis, 0, sizeof(ken_vis));
        for(int i = 0, j = 0; i < N; i++) {
            bool ok = true;
            for( ; j < N; j++) {
                if(!ken_vis[j] && dcmp(ken[j] - nao[i]) > 0) {
                    ok = false;
                    ken_vis[j] = true;
                    break;
                }
            }
            if(ok) scores_1++;
        }
        int scores_2 = 0;
        for(int i = N-1, j = N-1; j >= 0;) {
            if(dcmp(nao[i] - ken[j]) > 0) {
                i--;
                j--;
                scores_2++;
                continue;
            }
            j--;
        }
        printf("Case #%d: %d %d\n", ++kase, scores_2, scores_1);
    }
    return 0;
}

/*

4
1
0.5
0.6
2
0.7 0.2
0.8 0.3
3
0.5 0.1 0.9
0.6 0.4 0.3
9
0.186 0.389 0.907 0.832 0.959 0.557 0.300 0.992 0.899
0.916 0.728 0.271 0.520 0.700 0.521 0.215 0.341 0.458

Output

Case #1: 0 0
Case #2: 1 0
Case #3: 2 1
Case #4: 8 4
*/
