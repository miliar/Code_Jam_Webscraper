 
#include <iostream>
#include <string>
using namespace std;

string solve(string S) {
    string R = S.substr(0, 1);
    for (int i = 1; i < S.size(); i++) {
        if (S[i] < R[0])
            R = R + string(1, S[i]);
        else
            R = string(1, S[i]) + R;
    }
    return R;
}

int main() {
    int T, i;
    cin >> T;
    for (i = 0; i < T; i++) {
        string S;
        cin >> S;
        cout << "Case #" << (i + 1) << ": " << solve(S) << endl;
    }
    return 0;
}
