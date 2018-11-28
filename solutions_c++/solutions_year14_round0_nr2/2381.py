#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int rt = 1; rt <= T; ++ rt) {
        double C, F, X;
        cin >> C >> F >> X;
        double ans = 1e20;
        double time = 0, per = 2;
        for (int c = 0; c <= X; ++ c) {
            if (time + X / per < ans)
                ans = time + X / per;
            time += C / per;
            per += F;
        }
        printf("Case #%d: %.7lf\n", rt, ans);
    }
    return 0;
}
