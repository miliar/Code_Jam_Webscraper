#include <stdio.h>
#include <algorithm>
using namespace std;

int testsCnt;
int k, n, m;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    scanf("%d", &testsCnt);
    for (int testN = 1; testN <= testsCnt; testN++) {
        scanf("%d%d%d", &k, &n, &m);
        int w;
        if (k == 1) {
            w = 2;
        } else if (k >= 7) {
            w = 1;
        } else if ((n * m) % k) {
            w = 1;
        } else if (max(n, m) < k) {
            w = 1;
        } else if (min(n, m) * 2 + 1 <= k) {//!!!!!
            w = 1;
        } else if (k == 2) {
            w = 2;
        } else if (k == 3) {
            w = 2;
        } else if (min(n, m) * 2  <= k) {
            w = 1;
        } else {
            w = 2;
        }
        printf("Case #%d: %s\n", testN, w == 1 ? "RICHARD" : "GABRIEL");
    }
}