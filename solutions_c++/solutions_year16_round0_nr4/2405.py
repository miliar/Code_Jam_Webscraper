#include<iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    int n;
    int K, C, S;
    for(int cas = 1; cas <= T; cas++) {
        cin >> K >> C >> S;
        cout << "Case #" << cas << ": ";
        if(C == 1) {
            if(K == S) {
                for(int i = 1; i <= S; i++) {
                    cout << i << " ";
                }
            }
            else cout << "IMPOSSIBLE";
        }
        else {
            if(K == 1) {
                cout << 1;
            }
            else if(K-1 <= S) {
                for(int i = 2; i <= K; i++) {
                    cout << i << " ";
                }
            }
            else {
                cout << "IMPOSSIBLE";
            }
        }
        cout << "\n";
    }
}
