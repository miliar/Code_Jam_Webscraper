#include <cstdio>

int main()
{
    int T, kase = 1;
    scanf("%d", &T);

    while (T--) {
        int cand[17] = {0};
        int ans;
        scanf("%d", &ans);
        for (int r = 1; r <= 4; ++r) {
            for (int c = 1; c <= 4; ++c) {
                int num;
                scanf("%d", &num);
                if (r == ans) cand[num] = 1;
            }
        }
        int cnt = 0, real_ans;
        scanf("%d", &ans);
        for (int r = 1; r <= 4; ++r) {
            for (int c = 1; c <= 4; ++c) {
                int num;
                scanf("%d", &num);
                if (r == ans && cand[num]) {
                    ++cnt;
                    real_ans = num;
                }
            }
        }
        printf("Case #%d: ", kase++);
        if (cnt == 1) printf("%d\n", real_ans);
        else if (cnt > 1) printf("Bad magician!\n");
        else printf("Volunteer cheated!\n");
    }
}

