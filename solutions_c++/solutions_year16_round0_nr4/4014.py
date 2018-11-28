#include <iostream>
#include <string>

using namespace std;

int main() {
    
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int K, C, S;
        cin >> K >> C >> S;

        cout << "Case #" << t << ":";
        if (K == 1) {
            cout << " " << 1;
        } else {
            int N = (C == 1) ? K : K - 1;
            
            if (N > S) {
                cout << " IMPOSSIBLE";
            } else {
                for (int i = K + 1 - N; i <= K; i++) {
                    cout << " " << i;
                }
            }
        }
        cout << endl;
    }
    return 0;
}
