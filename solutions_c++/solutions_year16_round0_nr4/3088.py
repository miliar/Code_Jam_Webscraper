#include <iostream>

using namespace std;

int main() {
    int T;
    cin >> T;

    for (int t = 0; t < T; t++) {
        int K, C, S;
        cin >> K >> C >> S;

        cout << "Case #" << t + 1 << ":";
        for (int j = 0; j < K; j++) {
            cout << " " << j + 1;
        }
        cout << endl;
    }

    return 0;
}