#include <iostream>
#include <cstdio>

using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    for (int qqq = 1; qqq <= t; qqq++) {
        int d, arr[1000];
        scanf("%d", &d);
        for (int i = 0; i < d; i++)
            scanf("%d", arr + i);
        int L = 0, R = 1001;
        while (L < R - 1) {
            int M = (L + R) / 2;
            bool ok = false;
            for (int numR = 0; !ok && numR < M; numR++) {
                int repl = 0;
                for (int i = 0; repl <= numR && i < d; i++)
                    repl += (arr[i] - 1) / (M - numR);
                ok = (repl <= numR);
            }
            if (ok)
                R = M;
            else
                L = M;
        }
        printf("Case #%d: %d\n", qqq, R);
    }
    return 0;
}
