#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

int main() {
    int T, x, y;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d %d", &x, &y);
        printf("Case #%d: ", t);
        for (int i = 0; i < abs(x); i++) {
            if (x > 0)
                printf("WE");
            else
                printf("EW");
        }
        for (int i = 0; i < abs(y); i++) {
            if (y > 0)
                printf("SN");
            else
                printf("NS");
        }
        puts("");
    }
}
