#include <iostream>
using namespace std;

int T, K, C, S;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> T;
    for (int a = 1; a <= T; ++a) {
        cin >> K >> C >> S;
        cout << "Case #" << a << ":";
        for (int b = 1; b <= S; ++b)
            cout << " " << b;
        cout << "\n";
    }
    return 0;
}
