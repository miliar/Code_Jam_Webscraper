#include <iostream>

using namespace std;

int t;
int k, c, s;

int main() {
    cin >> t;
    for (int _ = 1; _ <= t; _++) {
        cin >> k >> c >> s;
        cout << "Case #" << _ << ": ";
        for (int i = 1; i <= k; i++) {
            cout << i << " ";
        }
        cout << endl;
    }
    return 0;
}