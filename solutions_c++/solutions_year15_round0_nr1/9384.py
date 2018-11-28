#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;

int T;
int SMAX;
string S;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> SMAX;
        cin >> S;
        int result = 0;
        int current = S[0] - '0';
        for (int i = 1; i <= SMAX; i++) {
            int digit = S[i] - '0';
            if (digit) {
                if (i > current + result) {
                    result += i - current - result;
                }
                current += digit;
            }
        }
        cout << "Case #" << t << ": " << result << endl;
    }

    return 0;
}
