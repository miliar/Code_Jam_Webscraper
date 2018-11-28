#include <iostream>
#include <string>

using namespace std;

void solve(string S) {
    char pre = '+';
    int res = 0;
    for (int i=0; i<S.length(); ++i) {
        if (pre == '+' && S[i] == '-') {
            if (i == 0)
                res += 1;
            else
                res += 2;
        }
        pre = S[i];
    }
    cout << res << endl;
}

int main() {
    int T;
    cin >> T;
    for (int i=0; i<T; ++i) {
        string S;
        cin >> S;
        cout << "Case #" << i + 1 << ": ";
        solve(S);
    }
    return 0;
}