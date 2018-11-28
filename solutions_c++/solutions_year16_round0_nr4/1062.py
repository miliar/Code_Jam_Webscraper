// Written by Luis Garcia, 2016.
// OJ-ID: CJ1601D

#include <cstdio>

using namespace std;

int main() {
    int T, K, C, S;
    scanf("%d", &T);
    for (int _T = 1; _T <= T; ++_T) {
        scanf("%d %d %d", &K, &C, &S);
        printf("Case #%d:", _T);
        for (int i = 1; i <= S; ++i) printf(" %d", i);
        puts("");
    }

    return 0;
}
