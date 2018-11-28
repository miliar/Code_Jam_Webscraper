#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

const int MAXN = 10000 + 3;
const int w[5][5] = 
{
{0, 0, 0, 0, 0},
{0, 1, 2, 3, 4},
{0, 2,-1, 4,-3},
{0, 3,-4,-1, 2},
{0, 4, 3,-2,-1}
};
int n, m, f[MAXN];
char str[MAXN];

void work()
{
    f[0] = 1;
    for (int i = 1; i <= n; ++i) {
        int t = f[i-1] > 0 ? f[i-1] : -f[i-1];
        f[i] = w[t][str[i] - 'i' + 2];
        if (f[i-1] < 0) f[i] = -f[i];
    }
    if (f[n] != -1) {
        puts("NO");
        return;
    }
    else {
        for (int i = n-1; i >= 1; --i) {
            if (f[i] == 4) {
                for (int j = i-1; j >= 1; --j) {
                    if (f[j] == 2) {
                        puts("YES");
                        return;
                    }
                }
                puts("NO");
                return;
            }
        }
        puts("NO");
        return;
    }
}
void prework()
{
}
int main()
{
    int T;
    scanf("%d", &T);
    prework();
    for (int kase = 1; kase <= T; ++kase) {
        scanf("%d%d", &n, &m);
        scanf("%s", str+1);
        for (int i = 1; i < m; ++i) {
            strncpy(str+i*n+1, str+1, n);
        }
        n *= m;
        printf("Case #%d: ", kase);
        work();
    }
    return 0;
}

