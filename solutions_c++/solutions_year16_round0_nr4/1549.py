#include <iostream>
using namespace std;

long long pow(int b, int x) {
    long long res = 1;
    while (x--) {
        res *= b;
    }
    return res;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int K, C, S;
        cin >> K >> C >> S;
        cout << "Case #" << t << ":";
        for (int i = 0; i < K; i++) {
            cout << " " << 1 + i * pow(K, C-1);
        }
        cout << endl;
    }
    return 0;
}
