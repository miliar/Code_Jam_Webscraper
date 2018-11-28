#include <cstdio>
int main()
{
    int T, ans_1, ans_2, first[4][4], second[4][4], number[16], ans[4], k;
    scanf("%d", &T);
    for (int n = 1; n <= T; n++) {
        for (int i = 0; i < 16; i++)
            number[i] = 0;
        for (int i = 0; i < 4; i++)
            ans[i] = 0;
        k = 0;
        scanf("%d", &ans_1);
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                scanf("%d", &first[i][j]);
        scanf("%d", &ans_2);
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                scanf("%d", &second[i][j]);
        for (int i = 0; i < 4; i++) {
            number[first[ans_1 - 1][i] - 1]++;
            number[second[ans_2 - 1][i] - 1]++;
        }
        for (int i = 0; i < 16; i++)
            if (number[i] == 2) {
                ans[k] = i + 1;
                k++;
            }
        printf("Case #%d: ", n);
        if (ans[0] == 0)
            printf("Volunteer cheated!\n");
        else if (ans[1] == 0)
            printf("%d\n", ans[0]);
        else
            printf("Bad magician!\n");
    }
    return 0;
}
