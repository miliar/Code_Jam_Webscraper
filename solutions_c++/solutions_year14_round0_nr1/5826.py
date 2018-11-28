#include <iostream>
#include <fstream>
#include <cstdio>
#include <string>

using namespace std;

int m1[4][4];
int m2[4][4];
int r1, r2;
int T;

int cnt[17];

int calc()
{
    memset(cnt, 0, sizeof(cnt));
    for (int i = 0; i < 4; i++) {
        cnt[m1[r1][i]]++;
        cnt[m2[r2][i]]++;
    }
    int ans = -2;
    for (int i = 1; i <= 16; i++)
        if (cnt[i] == 2) {
            if (ans == -2)
                ans = i;
            else {
                ans = -1;
                break;
            }
        }
    return ans;
}

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-out.txt", "w", stdout);
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        scanf("%d", &r1);
        r1--;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                scanf("%d", &(m1[i][j]));
        scanf("%d", &r2);
        r2--;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                scanf("%d", &(m2[i][j]));
        int ans = calc();
        if (ans == -1) {
            printf("Bad magician!\n");
        }
        else if (ans== -2) {
            printf("Volunteer cheated!\n");
        }
        else {
            printf("%d\n", ans);
        }
    }
    return 0;
}