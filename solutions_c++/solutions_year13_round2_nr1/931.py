#include <iostream>
#include <algorithm>
#include <stdio.h>

using namespace std;

int main() {
    int t;
    int r[100];
    cin >> t;
    for (int i = 0; i < t; i++) {
        int a, n;
        cin >> a >> n;
        for (int i = 0; i < n; i++)
            cin >> r[i];

        sort(r, r + n);

        int cur = 0, res = n;
        int curres = n;
        while (true) {
            while ((cur != n) && (r[cur] < a)) {
                a += r[cur];
                curres--;
                cur++;
            }

            res = min(curres, res);
            if (cur == n)
                break;

            if (a <= 1)
                break;
            while (a <= r[cur]) {
                a += (a - 1);
                curres++;
            }
        }

        printf("Case #%d: %d\n", i + 1, res);
    }
    return 0;
}
