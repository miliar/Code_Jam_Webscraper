#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define N 2600

int cnt[N];
int a[100][100];
int n;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-0.out", "w", stdout);
    int T, i, j, ca = 1;
    scanf("%d", &T);
    while (T--) {
        scanf("%d", &n);
        memset(cnt, 0, sizeof(cnt));
        for (i = 0;i < 2*n-1;i++) {
            for (j = 0;j < n;j++) {
                scanf("%d", &a[i][j]);
                cnt[a[i][j]]++;
            }
        }
        printf("Case #%d:", ca++);
        for (i = 1;i < N;i++) {
            if (cnt[i]&1) printf(" %d", i);
        }
        puts("");
    }
}
