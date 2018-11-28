#include <iostream>
using  namespace std;

void solve(int t) {
    int S[1100];
    int Smax;
    int a = 0;
    int g = 0;
    int s = 0;
    int f = 0;

    cin >> Smax;
    for (int k = 0; k <= Smax; k++) {
        scanf("%1d", &s);
        if (s == 0) {
            continue;
        }
        g = max(0, k - a);
        f += g;
//        printf("g: %d ", g);
        a += g + s;
//        printf("a: %d ::: ", a);
    }
    printf("Case #%d: %d\n", t, f);
}

int main() {
    int T;

    cin >> T;
    for (int i = 0; i < T; i++) {
        solve(i + 1);
    }
    return 0;
}
