#include <iostream>
#include <cstring>
using namespace std;

int f[10];

void update_f(int a) {
    while (a) {
        f[a % 10] += 1;
        a /= 10;
    }
}

bool count_all() {
    for (int i = 0; i < 10; i++) {
        if (!f[i]) return false;
    }
    return true;
}

int proc(int a) {
    memset(f, 0, sizeof f);
    int b = a;
    while (true) {
        update_f(b);
        if (count_all()) return b;
        b += a;
    }
}

int main() {
    int t, a;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cin >> a;
        cout << "Case #" << i << ": ";
        if (!a) cout << "INSOMNIA" << endl;
        else cout << proc(a) << endl;
    }
    return 0;
}
