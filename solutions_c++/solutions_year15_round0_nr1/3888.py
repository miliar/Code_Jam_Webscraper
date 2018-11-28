#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
using namespace std;

int main () {
    int T;
    cin >> T;

    for (int tt = 1; tt <= T; ++tt) {
        int maxs;
        string s;
        cin >> maxs >> s;

        int curaud = 0;
        int guests = 0;
        for (int i = 0; i <= maxs; ++i) {
            if (curaud < i) {
                guests += i - curaud;
                curaud += i - curaud;
            }

            curaud += (int)(s[i] - '0');
        }

        printf("Case #%d: %d\n", tt, guests);
    }

    return 0;
}
