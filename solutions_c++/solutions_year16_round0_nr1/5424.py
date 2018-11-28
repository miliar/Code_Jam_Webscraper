#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <algorithm>
#include <deque>
#include <cmath>
#include <ctime>

using namespace std;

int main() {
    freopen("A-large (1).in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tests;
    cin >> tests;
    for (int test = 0; test < tests; test++) {
        cout << "Case #" << test + 1 << ": ";
        bool used[10];
        for (int i = 0; i < 10; ++i) used[i] = false;
        int n;
        cin >> n;
        if (n == 0) {
            cout << "INSOMNIA\n";
            continue;
        }
        int cur = 1;
        while (true) {
            int n_copy = n * cur;
            while (n_copy != 0) {
                int d = n_copy % 10;
                used[d] = true;
                n_copy = n_copy / 10;
            }
            int flag = 0;
            for (int i = 0; i < 10; ++i) {
                if (!used[i]) {
                    flag = 1;
                }
            }
            if (flag == 0) {
                cout << cur * n;
                break;
            } else {
                cur++;
            }
        }
        cout << "\n";
    }
    return 0;
}