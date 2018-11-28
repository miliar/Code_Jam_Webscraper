#include <bits/stdc++.h>

using namespace std;

void go() {
    int k, c, s;
    scanf("%d%d%d", &k, &c, &s);
    for(int i = 1; i <= s; i++) printf(" %d", i);
    printf("\n");
}

int main() {
    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++) {
        printf("Case #%d:", t);
        go();
    }
    return 0;
}
