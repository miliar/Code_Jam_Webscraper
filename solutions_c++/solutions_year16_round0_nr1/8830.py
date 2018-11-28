#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

void solve() {
    int n;
    cin >> n;

    if (n == 0) {
        cout << "INSOMNIA";
        return;
    }

    int wasTotal = 0;
    vector <char> was(10, 0);

    int k, s, tmp;
    for (k = 0, s = n; wasTotal < 10 && k <= 1000; ++k, s += n) {
        tmp = s;
        while (tmp) {
            if (!was[tmp % 10]) {
                wasTotal++;
                was[tmp % 10] = 1;
            }
            tmp /= 10;
        }
    }
    if (wasTotal != 10)
        cout << "INSOMNIA";
    else
        cout << s - n;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T, test;
    for (cin >> T, test = 1; test <= T; ++test) {
        cout << "Case #" << test << ": ";
        solve();
        cout << "\n";
    }
    return 0;
}
