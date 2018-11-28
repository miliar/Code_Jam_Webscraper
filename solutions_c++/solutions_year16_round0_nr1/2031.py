#include <iostream>
#include <stdio.h>

using namespace std;

bool found[10];

void match_digits(long long n) {
    while (n > 0) {
        found[n % 10] = true;
        n /= 10;
    }
}

void reset_digits() {
    for (int i = 0; i < 10; i++)
        found[i] = false;
}
bool good() {
    for (int i = 0; i < 10; i++)
        if (!found[i])
            return false;
    return true;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n;
    long long k;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> k;
        cout << "CASE #" << i << ": ";
        if (k == 0) {
            cout << "INSOMNIA" << endl;
            continue;
        }
        reset_digits();
        bool zbs = false;
        long long cur = 0;
        for (int j = 1; j <= 1000000; j++) {
            cur += k;
            match_digits(cur);
            if (good()) {
                zbs = true;
                break;
            }
        }
        if (!zbs) {
            cout << "INSOMNIA" << endl;
        } else {
            cout << cur << endl;
        }
    }
}
