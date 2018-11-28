#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char ch[3];
char ans[(1 <<20) + 5];
char out[(1 << 20) + 5];
int cnt[3];
int tot[3];

bool Try(int n, int win, int l, int r) {
    int lose = (win + 1) % 3;
    if (n == 1) {
        if (cnt[win] > 0 && cnt[lose] > 0) {
            cnt[win]--;
            cnt[lose]--;
            ans[l] = ch[win];
            ans[l + 1] = ch[lose];
            return true;
        } else return false;
    }
    return Try(n - 1, win, l, l + (1 << n - 1)) && Try(n - 1, lose, l + (1 << n - 1), r);
}

bool Pass(int b[], int n) {
    int a[10] = {0};
    for (int i = 0; i < (1 << n); i++) {
            a[i] = b[i];
            //printf("%d ", a[i]); puts("");
    }
    for (int i = n; i > 0; i--)
        for (int j = 0; j < (1 << i); j += 2)
            if (a[j] == a[j + 1]) return false;
            else if ((a[j] + 1) % 3 == a[j + 1]) a[j / 2] = a[j + 1];
                else a[j / 2] = a[j];
    return true;
}

void Test(int n) {
    int t = 0;
    int a[10] = {0};

    for (int i = 0; i < 3; i++)
        for (int j = 0; j < tot[i]; j++)
            a[t++] = i;
    bool flag = false;
    do {
        if (Pass(a, n)) {
            for (int j = 0; j < t; j++)
                printf("%c", ch[a[j]]);
            puts("");
            flag = true;
            break;
        }
    } while (next_permutation(a, a + t));
    if (!flag) puts("IMPOSSIBLE");
}

int main() {
    int T = 0;
    scanf("%d", &T);
    ch[0] = 'P'; ch[1] = 'R'; ch[2] = 'S';
    for (int cas = 1; cas <= T; cas++) {
        int n = 0;
        scanf("%d%d%d%d", &n, &tot[1], &tot[0], &tot[2]);
        bool flag = false;
        ans[1 << n] = '\0';
        for (int win = 0; win < 3; win++) {
            for (int i = 0; i < 3; i++) cnt[i] = tot[i];
            if (Try(n, win, 0, 1 << n)) {
                flag = true;
                break;
            }
        }
        if (!flag) printf("Case #%d: IMPOSSIBLE\n", cas);
        else {
            for (int i = 0; i < n; i++) {
                int len = 1 << i;
                for (int j = 0; j < (1 << n); j += len * 2)
                    if (strncmp(ans + j, ans + j + len, len) > 0) {
                        strncpy(out + j, ans + j, len);
                        strncpy(ans + j, ans + j + len, len);
                        strncpy(ans + j + len, out + j, len);
                    }
            }
            printf("Case #%d: %s\n", cas, ans);
        }
        //printf("Case #%d: ", cas);Test(n);
    }
    return 0;
}
