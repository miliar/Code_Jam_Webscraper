#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

void solve(int x, int y) {
    for (int i = 0; i < abs(x); i++)
        if (x > 0)
            printf("WE");
        else
            printf("EW");

    for (int i = 0; i < abs(y); i++)
        if (y > 0)
            printf("SN");
        else
            printf("NS");
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        int x, y;
        cin >> x >> y;
        printf("Case #%d: ", i);
        solve(x, y);
        printf("\n");
    }
    return 0;
}
