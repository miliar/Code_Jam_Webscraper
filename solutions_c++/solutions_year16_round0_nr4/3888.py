#include <iostream>

using namespace std;

int main() {
    size_t T, K, C, S;
    cin >> T;
    for (size_t t = 0; t < T; t++) {
        cin >> K >> C >> S;
        cout << "Case #" << t + 1 << ":";
        for (size_t i = 0; i < K; i++) {
            cout << " " << i + 1;
        }
        cout << endl;
    }
}
