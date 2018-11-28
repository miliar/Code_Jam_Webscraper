#include <cstdio>

int main() {
    
    int testCases;
    
    scanf("%d", &testCases);
    
    for (int testCase = 1; testCase <= testCases; ++testCase) {

        int x, r, c;

        scanf("%d %d %d", &x, &r, &c);

        printf("Case #%d: ", testCase);

        if (x == 1) {
            printf("GABRIEL\n");
        }
        else if (x == 2) {
            if (r * c & 1) {
                printf("RICHARD\n");
            }
            else {
                printf("GABRIEL\n");
            }
        }
        else if (x == 3) {
            if (r * c % 3 == 0) {
                if (r == 1 || c == 1) {
                    printf("RICHARD\n");
                }
                else {
                    printf("GABRIEL\n");
                }
            }
            else {
                printf("RICHARD\n");
            }
        }
        else if (x == 4) {
            if (r * c % 4 != 0) {
                printf("RICHARD\n");
            }
            else {
                if (r * c >= 12) {
                    printf("GABRIEL\n");
                }
                else {
                    printf("RICHARD\n");
                }
            }
        }

    }
    
    return 0;
    
}
