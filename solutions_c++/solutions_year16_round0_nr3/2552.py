#include <cstdio>
#include <set>
#include <cstdlib>

using namespace std;

set<long long> vst;

const int MAXN = 1000000;

int d[40];
char a[40];

int f[MAXN + 1] = {0};
int prime[MAXN] = {};
int pn = 0;

long long Base(char a[], int n, int b) {
    long long ret = 0;
    for (int i = 0; i < n; i++)
        ret = ret * (long long)b + (long long)(a[i] - '0');
    return ret;
}

int Find_divisor(long long val) {
    if (val <= MAXN) return f[val];
    for (int i = 0; i < pn; i++)
        if (val % prime[i] == 0) return prime[i];
    return 0;
}

int main() {
    for (int i = 2; i <= MAXN / i; i++)
        if (f[i] == 0) for (int j = 2; j <= MAXN / i; j++)
                            f[i * j] = i;
    for (int i = 2; i <= MAXN; i++)
        if (f[i] == 0) prime[pn++] = i;
    int T = 0;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        vst.clear();
        int n, j;
        scanf("%d%d", &n, &j);
        printf("Case #%d:\n", cas);
        while (j > 0) {
            a[n] = '\0';
            a[0] = a[n - 1] = '1';
            for (int i = 1; i < n - 1; i++)
                a[i] = '0' + rand() % 2;
            bool flag = true;
            for (int b = 2; b <= 10; b++) {
                long long val = Base(a, n, b);
                if (b == 2) {
                    if (vst.find(val) != vst.end()) {
                        flag = false;
                        break;
                    }
                    vst.insert(val);
                }
                d[b] = Find_divisor(val);
                if (d[b] == 0) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                printf("%s", a);
                for (int b = 2; b <= 10; b++) {
                    printf(" %d" , d[b]);
                }
                puts("");
                j--;
            }
        }
    }
    return 0;
}
