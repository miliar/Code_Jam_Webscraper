#include <iostream>
#include <vector>

using namespace std;

void f(long long n, vector<bool> &d, int& s) {
    while (n > 0) {
        d[n % 10] = 1;
        n /= 10;
    }
    s = 0;
    for (int i = 0; i < 10; i++) {
        s += d[i];
    }
}

int main() {
    freopen("/home/artur/Загрузки/A-large.in", "r", stdin);
    freopen("/home/artur/Загрузки/output.txt", "w", stdout);
    int TESTS, t;
    long long cur;
    cin >> TESTS;
    for (int test = 1; test <= TESTS; test++) {
        cout << "Case #" << test << ": ";
        cin >> t;
        if (t == 0) {
            cout << "INSOMNIA" << endl;
            continue;
        }
        vector<bool> d(10);
        int s = 0;
        cur = t;
        f(cur, d, s);
        while (s < 10) {
            cur += t;
            f(cur, d, s);
        }
        cout << cur << endl;
    }
    return 0;
}