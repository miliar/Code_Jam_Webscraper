#include <iostream>
using namespace std;

int cc = 0;
bool flag[10];

void add(int x) {
    while (x) {
        if (!flag[x % 10]) {
            flag[x % 10] = 1;
            cc++;
        }
        x /= 10;
    }
}

int main() {
    int t, x;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cin >> x;
        if (x == 0) {
            printf("Case #%d: INSOMNIA\n", i);
            continue;
        }
        memset(flag, 0, 10);
        cc = 0;
        for (int j = x;; j += x) {
            add(j);
            if (cc == 10) {
                printf("Case #%d: %d\n", i, j);
                break;
            }
        }
    }
}

