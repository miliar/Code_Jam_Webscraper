#include <stdio.h>
#include <iostream>

#define NMAX 1001

using namespace std;

void clearPluses(char* s, int &top) {
    while(-1 < top && '+' == s[top]) {
        --top;
    }
}

void flip(char* s, int top, int flipLength) {
    for (int it = 0; it < flipLength; ++it) {
        s[top - it] = '+' == s[top - it] ? '-' : '+';
    }
}

int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);

    char s[NMAX];
    int tests, K, flips, top;
    string pancakes;

    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        cin >> pancakes >> K;
        flips = 0;
        top = -1;

        for (int it = 0; it < pancakes.size(); ++it) {
            s[++top] = pancakes[it];
        }

        clearPluses(s, top);
        while (K <= (top + 1) && '-' == s[top]) {
            ++flips;
            flip(s, top, K);
            clearPluses(s, top);
        }
        clearPluses(s, top);

        cout << "Case #" << test << ": " ;
        if (-1 == top) {
            cout << flips;
        } else {
            cout << "IMPOSSIBLE";
        }
        cout << endl;
    }

    return 0;
}
