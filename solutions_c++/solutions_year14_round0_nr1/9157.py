#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int mp[5][5];
int a[5];
int main() {
    freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
    int T, n;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%d", &n);
        for (int i = 1; i <= 4; i++) {
            for (int j = 1; j <= 4; j++) {
                scanf("%d", &mp[i][j]);
            }
        }
        for (int i = 1; i <= 4; i++) {
            a[i] = mp[n][i];
        }
        scanf("%d", &n);
        for (int i = 1; i <= 4; i++) {
            for (int j = 1; j <= 4; j++) {
                scanf("%d", &mp[i][j]);
            }
        }
        int cnt = 0, x;
        for (int i = 1; i <= 4; i++) {
            for (int j = 1; j <= 4; j++) {
                if (a[i] == mp[n][j]) {
                    cnt++;
                    x = a[i];
                }
            }
        }
        printf("Case #%d: ", cas);
        if (cnt == 1) {
            printf("%d\n", x);
        }else if (cnt >= 2) {
            printf("Bad magician!\n");
        }else {
            printf("Volunteer cheated!\n");
        }
    }
    return 0;
}
