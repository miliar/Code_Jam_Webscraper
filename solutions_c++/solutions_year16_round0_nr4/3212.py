#include <iostream>
#include <cstdio>

using namespace std;


int solve(int tc) {
    int k,c,s;
    scanf("%d %d %d", &k, &c, &s);
    printf("Case #%d:", tc);
    for (int i=1; i<=k; i++) {
        printf(" %d", i);
    }
    printf("\n");
    return 0;
}


int main() {
    int T;
    scanf("%d", &T);
    for (int i = 1; i<=T; i++) {
        solve(i);
    }
    return 0;
}
