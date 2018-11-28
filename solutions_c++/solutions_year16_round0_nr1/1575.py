#include <iostream>
using namespace std;

int T, N;
int mask;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> T;
    for (int a = 1; a <= T; ++a) {
        cin >> N;
        if (N == 0) { cout << "Case #" << a << ": INSOMNIA\n"; continue; }
        mask = 0;
        for (int b = 1; ; ++b) {
            if (N * b >= 1e9) cerr << "Overflow warning!\n";
            int TMP = N * b;
            while (TMP) {
                mask |= (1 << (TMP % 10));
                TMP /= 10;
            }
            if (mask == ((1 << 10) - 1)) {
                cout << "Case #" << a << ": " << N * b << "\n";
                break;
            }
        }
    }
    return 0;
}
