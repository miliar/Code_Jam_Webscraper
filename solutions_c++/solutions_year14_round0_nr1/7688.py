#include <cstdio>
#include <cstring>

int TC, ans, cnt_ans, r, cnt[20];

void read_card(int row) {
    int x;
    for (int i = 1; i <= 4; i++)
        for (int j = 1; j <= 4; j++) {
            scanf("%d", &x);
            if (i == row)
                cnt[x]++;
        }
}

int main() {
    scanf("%d", &TC);
    for (int tc = 1; tc <= TC; tc++) {
        memset(cnt, 0, sizeof cnt);
        scanf("%d", &r);
        read_card(r);
        scanf("%d", &r);
        read_card(r);
        ans = -1;
        cnt_ans = 0;
        for (int i = 1; i <= 16; i++)
            if (cnt[i] == 2) {
                cnt_ans++;
                ans = i;
            }
        printf("Case #%d: ", tc);
        if (cnt_ans == 1)
            printf("%d\n", ans);
        else if (cnt_ans == 0)
            printf("Volunteer cheated!\n");
        else
            printf("Bad magician!\n");
    }
}