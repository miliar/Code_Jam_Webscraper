#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

int MinW(long long p, int n) {
    long long cur = (1ll << n) - 1;
    int c = 0;
    while (cur >= p) {
        c++;
        cur -= 1ll << n - c;
    }
    return c;
}

int MinL(long long p, int n) {
    long long cur = 0;
    int c = 0;
    while (cur < p && c < n) {
        c++;
        cur += 1ll << n - c;
    }
    return c;
}

int T, cas;

void run() {
    int n;
    long long p;
    cin >> n >> p;
    if (p < (1ll << n)) {
        int w = MinW(p, n);
        int l = MinL(p, n);
        cout << "Case #" << cas << ": " << (1ll << l) - 2 << " " << (1ll << n) - (1ll << w) << endl;
    } else
        cout << "Case #" << cas << ": " << p - 1 << " " << p - 1 << endl;
}

int main() {
    cin >> T;
    for (cas = 1; cas <= T; cas++)
        run();
    return 0;
}
