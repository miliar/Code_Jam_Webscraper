#define TXTOUT
#include<bits/stdc++.h>
using namespace std;
const int M = 1e3 + 10;
char a[M];
int n;
int Solve() {
    int sum = 0;
    int la = strlen(a);
    for (int i = 0; i + n - 1 < la; i++) {
        if (a[i] == '+') continue;
        sum++;
        for (int j = 0; j < n; j++) {
            if (a[i + j] == '+') {
                a[i + j] = '-';
            } else {
                a[i + j] = '+';
            }
        }
    }
    for (int i = 0; i < la; i++) {
        if (a[i] == '-') sum = -1;
    }
    return sum;
}
int main() {
    #ifdef TXTOUT
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    #endif // TXTOUT
    int t;
    scanf("%d", &t);
    int cas = 1;
    while (t--) {
        scanf("%s%d", a, &n);
        printf("Case #%d: ", cas++);
        int answer = Solve();
        if (answer == -1) {
            puts("IMPOSSIBLE");
        } else {
            printf("%d\n", answer);
        }
    }
    return 0;
}

/**

4
132
1000
7
111111111111111110

*/
