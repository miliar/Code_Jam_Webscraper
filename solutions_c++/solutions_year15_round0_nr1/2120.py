#include <iostream>
#include <stdio.h>

#if 0
#include <boost/>
#endif

using namespace std;

int T;

int solve() {
    int Smax, total = 0, add = 0;
    cin >> Smax;

    for (int i = 0; i <= Smax; ++i) {
        char ch;
        do {
            cin.read(&ch, 1);
        } while (!isdigit(ch));

        if (total < i) {
            add += (i - total);
            total = i;
        }
        total += (ch - '0');
    }
    return add;
}

int main(int argc, char* argv[]) {
    cin >> T;
    for (int t = 0; t != T; ++t) {
        int s = solve();
        if (s == -1)
            printf("Case #%d: I don't know.\n", t + 1);
        else
            printf("Case #%d: %d\n", t + 1, s);
    }
    return 0;
}

