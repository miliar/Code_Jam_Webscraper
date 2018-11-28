#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include <string>

using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    register int i, cases;
    for (cases = 0; cases < T; cases++) {
        int Smax, standing = 0, needed = 0;
        scanf("%d ", &Smax);
        for (i = 0; i <= Smax; i++) {
            int count = getchar() - '0';
            if (count && standing + needed < i)
                needed = i - standing;
            standing += count;
        }
        printf("Case #%d: %d\n", cases + 1, needed);
    }
}
