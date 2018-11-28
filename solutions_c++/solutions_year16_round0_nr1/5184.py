#include <iostream>

using namespace std;

#define long unsigned long long

/*
5
0
1
2
11
1692
 */

int EZMask = 0;

void EZClear() {
    EZMask = 0;
}

bool EZAll() {
    return EZMask == (1 << 10) - 1;
}

void EZAdd(long n) {
    string s = to_string(n);
    for (char c : s) {
        int d = c - '0';
        EZMask |= (1 << d);
    }
}


int main() {
    int t;
    long n;
    cin >> t;
    for (int test = 0; test < t; ++test) {
        cin >> n;
        cout << "Case #" << test + 1 << ": ";
        if (n == 0) {
            cout << "INSOMNIA";
        } else {
            EZClear();
            for (int i = 1; i < 1000; ++i) {
                long c = n * i;

                EZAdd(c);
                if (EZAll()) {
                    cout << c;
                    break;
                }
            }
        }

        cout << endl;
    }
    return 0;
}