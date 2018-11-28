#include <iostream>
#include <cstdio>

using namespace std;

int a[4], b[4], ans;

int func()
{
    int count = 0;

     for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {

                if (a[i] == b[j]) {
                    count++;
                    ans = a[i];
                }
            }
     }

     return count;
}

int main()
{
    int t, n, c = 0;

    scanf("%d", &t);

    while (t--) {
        c++;
        scanf("%d", &n);
        int x;

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                scanf("%d", &x);

                if (i == n - 1) {
                    a[j] = x;
                }
            }
        }

        scanf("%d", &n);

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                scanf("%d", &x);

                if (i == n - 1) {
                    b[j] = x;
                }
            }
        }

        n = func();

        if (n == 1) {
            printf("Case #%d: %d\n", (c), ans);
        } else if (n == 0) {
             printf("Case #%d: Volunteer cheated!\n", (c));
        } else {
            printf("Case #%d: Bad magician!\n", (c));
        }

    }

    return 0;
}
