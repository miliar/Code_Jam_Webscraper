#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);

    int t, a, b, A[16], B[16], cnt, ans;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        scanf("%d", &a); a--;
        for (int j = 0; j < 16; j++) scanf("%d", &A[j]);
        scanf("%d", &b); b--;
        for (int j = 0; j < 16; j++) scanf("%d", &B[j]);
        cnt = 0;
        for (int j = 0; j < 4; j++)
            for (int k = 0; k < 4; k++)
                if (A[(a << 2) + j] == B[(b << 2) + k]) cnt++, ans = A[(a << 2) + j];
        if (cnt == 1)
            printf("Case #%d: %d\n", i, ans);
        else if (!cnt)
            printf("Case #%d: %s\n", i, "Volunteer cheated!");
        else
            printf("Case #%d: %s\n", i, "Bad magician!");
    }
    return 0;
}
