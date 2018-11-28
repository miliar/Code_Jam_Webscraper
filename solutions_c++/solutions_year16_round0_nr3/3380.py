#include <iostream>

using namespace std;

int main() {
    int T, N, J;
    cin >> T >> N >> J;

    cout << "Case #1:" << endl;

    N = (N - 2) / 2;

    for (int bits = 0; bits < J; ++bits) {
        cout << "1";
        int temp = bits;
        for (int i = 0; i < N; ++i) {
            if (temp % 2) {
                cout << "11";
            }
            else {
                cout << "00";
            }
            temp /= 2;
        }
        cout << "1 3 4 5 6 7 8 9 10 11" << endl;
    }
    return 0;
}
