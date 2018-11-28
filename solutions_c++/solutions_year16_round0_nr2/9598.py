#include <iostream>
#include <string>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        string S;
        cin >> S;

        int result = 0;
        char last = '+';
        for (auto it = S.rbegin(); it != S.rend(); ++it) {
            if (*it != last) {
                ++result;
                last = *it;
            }
        }

        cout << "Case #" << t + 1 << ": " << result << endl;
    }
}