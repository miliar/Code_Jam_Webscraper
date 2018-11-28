#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    int T;

    cin >> T;

    for (int i = 1; i <= T; i++) {
        printf("Case #%d: ", i);

        string S;
        cin >> S;

        string out;

        out.push_back(S[0]);

        for (int j = 1; j < S.length(); j++) {
            char c = S[j];

            if (c < out.front()) {
                out.push_back(c);
            } else {
                out = c + out;
            }
        }

        cout << out << endl;
    }
}
