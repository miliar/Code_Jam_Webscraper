#include <iostream>
#include <fstream>
#include <cstdio>
#include <string.h>
using namespace std;

int main() {
    freopen("ta.txt", "r", stdin);
    freopen("ans.txt", "w", stdout);
    int t, r1, r2, tmp, ans;
    bool h[17];
    scanf("%d", &t);
    for (int z = 1; z <= t; z++) {
        cin >> r1;

        memset(h, false, sizeof(h));
        ans = -1;

        for (int i = 1; i <= 4; i++) {
            for (int j = 1; j <= 4; j++) {
                scanf("%d", &tmp);
                if (i == r1)
                    h[tmp] = true;
            }
        }

        cin >> r2;
        for (int i = 1; i <= 4; i++) {
            for (int j = 1; j <= 4; j++) {
                scanf("%d", &tmp);
                if (i == r2 && h[tmp] == true) {
                    if (ans == -1)
                        ans = tmp;
                    else
                        ans = -2;
                }
            }
        }
        printf("Case #%d: ", z);
        if (ans == -1)
            printf("Volunteer cheated!\n");
        else if (ans == -2)
            printf("Bad magician!\n");
        else
            printf("%d\n", ans);
    }
    return 0;
}
