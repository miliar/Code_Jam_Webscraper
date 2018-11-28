#include <iostream>
#include <string>
using namespace std;

int T, K;
string S;

void flip(int X) {
    for (int a = 0; a < K; ++a)
        S[X + a] = (S[X + a] == '-' ? '+' : '-');
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> T;
    for (int TT = 1; TT <= T; ++TT) {
        cin >> S >> K;
        bool valid = true;
        int CNT = 0;
        for (int a = 0; a < (int)S.size(); ++a) {
            if (S[a] == '+') continue;
            if (a + K > (int)S.size())
                valid = false;
            else {
                ++CNT;
                flip(a);
            }
        }
        cout << "Case #" << TT << ": ";
        if (valid) cout << CNT << "\n";
        else cout << "IMPOSSIBLE\n";
    }
    return 0;
}
