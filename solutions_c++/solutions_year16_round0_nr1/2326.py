#include <bits/stdc++.h>

using std::cin;

const int ALL = 0x3ff;

void solve(int n) {
    if (n == 0) {
        puts("INSOMNIA");
        return;
    }
    int appeared = 0, current = 0;
    /* assume that we will got the answer before overflow */
    for (int temp; appeared != ALL; ) {
        current += n;
        // for test purpose
        // if (current < 0)
            // *(int *)0 = 0;
        temp = current;
        while (temp) {
            appeared |= 1 << (temp % 10);
            temp /= 10;
        }
    }
    std::cout << current << std::endl;
}

int main() {
    int t, n;
    cin >> t;
    for (int ti = 1; ti <= t; ++ti) {
        cin >> n;
        std::cout << "Case #" << ti << ": ";
        solve(n);
    }
}
