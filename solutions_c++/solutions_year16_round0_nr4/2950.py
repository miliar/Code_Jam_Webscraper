#include <iostream>
#include <cstdio>

using namespace std;

int main(void) {
    int T, K, C, S;
    scanf("%d", &T);
    for (int i=1; i<=T; i++) {
        scanf ("%d%d%d", &K, &C, &S);
        printf ("Case #%d:", i);
        for(int j=1; j<=S; j++) {
            printf(" %d", j);
        }
        printf("\n");
    }
    return 0;
}
