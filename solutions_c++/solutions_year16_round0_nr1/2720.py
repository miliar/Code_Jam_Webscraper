#include <iostream>

using namespace std;


void count(int y) {
    bool saw[10] = {false};
    int n = y;
    for (int i = 2; i < 10000; ++i) {
        int j = 0;
        int x = n;
        do {
            saw[x % 10] = true;
            x /= 10;
        } while (x);
        for (; j < 10; j++) {
            if (!saw[j])
                break;
        }
        n += y;
        if (j < 10)
            continue;
        cout << n - y;
        return;
    }
    cout << "INSOMNIA";
}

int main() {
    int n, t;

    cin >> n;

    for (int i = 1; i <= n; ++i) {
        cin >> t;
        cout << "Case #" << i << ": ";
        count(t);
        cout << '\n';
    }
}
