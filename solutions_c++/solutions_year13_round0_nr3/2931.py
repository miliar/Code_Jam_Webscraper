#include <iostream>
#include <stdio.h>
#include <ctype.h>
#include <math.h>
using namespace std;

int stored[1005];

int isPalli(int num) {
    int temp = num, i = 0, d, rev = 0;
    while (num) {
        d = num % 10;
        rev = rev * 10 + d;
        num /= 10;
        i++;
    }
    if (temp == rev) return 1;
    return 0;
}

void precalc() {
    for (int i = 0; i <= 1001; i++) stored[i] = 0;
    for (int i = 1; i <= 1000; i++) {
        if (isPalli(i)) { // is pallindrome
            int sqrtnum = sqrt(i);
            if (sqrtnum == sqrt(i)) { // is perfect square 
                if (isPalli(sqrtnum)) // sqrt root also pallindrome
                    stored[i] = 1;
            }
        }
    }
}

int main(void) {
    int t, a, b;
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w+", stdout);

    precalc();

    cin >> t;
    for (int i = 1; i <= t; i++) {
        int res = 0;
        cin >> a >> b;

        for (int j = a; j <= b; j++)
            if (stored[j] == 1) res++;

        cout << "Case #" << i << ": " << res << "\n";
    }
    return 0;
}

