#include <cstring>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

// return True --> GABRIEL
int check(int R, int C, int X) {
    if (R == 1 && C == 1) return X == 1;
    if (R == 1 && C == 2) return X <= 2;
    if (R == 1 && C == 3) return X == 1;
    if (R == 1 && C == 4) return X <= 2;
    if (R == 2 && C == 2) return X <= 2;
    if (R == 2 && C == 3) return X <= 3;
    if (R == 2 && C == 4) return X <= 2;
    if (R == 3 && C == 3) return X == 1 || X == 3;
    if (R == 3 && C == 4) return true;
    if (R == 4 && C == 4) return X != 3;
    printf("error\n");
    return true;
}

int main() {
    int T;
    scanf("%d", &T);    
    for (int test = 1; test <= T; ++ test) {
        int r, c, x;
        scanf("%d %d %d", &x, &r, &c);
        if (r > c) {
            int k = r; r = c; c = k;
        }
        if (check(r, c, x))
            printf("Case #%d: GABRIEL\n", test);
        else
            printf("Case #%d: RICHARD\n", test);

    }
    return 0;
}