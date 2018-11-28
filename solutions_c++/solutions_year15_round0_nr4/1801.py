#include <iostream>
#include <cstdio>
using namespace std;
void Solve(int no) {
    int X, R, C;
    scanf("%d %d %d", &X, &R, &C);
    if (X == 1) {
        printf("Case #%d: GABRIEL\n", no);
        return;
    }
    if (X == 2) {
        if (R*C % 2 == 0) {
            printf("Case #%d: GABRIEL\n", no);
        } else {
            printf("Case #%d: RICHARD\n", no);
        }
        return;
    }
    if (X == 3) {
        if (R*C == 6 || R*C==12 ||R*C == 9) {
            printf("Case #%d: GABRIEL\n", no);
        } else {
            printf("Case #%d: RICHARD\n", no);
        }
        return;
    }
    if (X == 4) {
        if (R*C == 12 || R*C == 16) {
            printf("Case #%d: GABRIEL\n", no);
        } else {
            printf("Case #%d: RICHARD\n", no);
        }
        return;
    }
    return;

}
int main() {
    int T;
    scanf("%d\n", &T);
    for (int i=0; i<T; i++) {
        Solve(i+1);
    }
    return 0;
}