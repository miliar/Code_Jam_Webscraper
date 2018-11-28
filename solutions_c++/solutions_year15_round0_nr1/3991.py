#include <iostream>

using namespace std;

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; ++i) {
        int maxLevel;
        cin >> maxLevel;

        string s;
        cin >> s;

        int numRequired = 0;
        int numStanding = 0;
        for (int j = 0; j < s.length(); ++j) {
            int num = s[j] - '0';
            if (numStanding < j) {
                numRequired += j - numStanding;
                numStanding = j + num;
            } else {
                numStanding += num;
            }
        }

        cout << "Case #" << i + 1 << ": " << numRequired << endl;
    }

    return 0;
}
