#include <bits/stdc++.h>
using namespace std;

bool check_small(int x, int r, int c) {
    if ((r * c) % x != 0)
        return true;
    else {
        if (x <= 2) 
            return false;
        else if (x == 3) {
            if (r < 3 && c < 3)
                return true;
            if (r == 1 || c == 1)
                return true;
            return false;
        } else if (x == 4) {
            if (r < 4 && c < 4)
                return true;
            if (r == 1 || c == 1)
                return true;
            if (r == 2 || c == 2)
                return true;
            return false;
        }
    }
}

int nTest;
int x, r, c;

int main() {

    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D_out.txt", "w", stdout);

    scanf("%d", &nTest);
    for (int test = 1; test <= nTest; test++) {
        scanf("%d%d%d", &x, &r, &c);
        if (check_small(x, r, c)) 
            printf("Case #%d: RICHARD\n", test);
        else 
            printf("Case #%d: GABRIEL\n", test);
    }

    return 0;
}