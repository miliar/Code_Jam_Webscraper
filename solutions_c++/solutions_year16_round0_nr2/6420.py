#include <iostream>
#include <string>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        string input;
        cin >> input;

        int ans = 0;
        int n = input.size();
        for (int i = n-1; i >= 0; --i) {
            if (input[i] == '-') {
                ans ++;
                for (int j = i; j >= 0; --j) {
                    if (input[j] == '-') input[j] = '+';
                    else input[j] = '-';
                }
            }
        }

        cout << "Case #" << t << ": " << ans << endl;
    }

    return 0;
}
