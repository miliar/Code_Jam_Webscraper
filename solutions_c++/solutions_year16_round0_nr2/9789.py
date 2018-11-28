#include <iostream>
#include <vector>

using namespace std;

int main() {
    int T;
    cin >> T;
    vector<int> results;
    for (int i = 0; i < T; i++) {
        string s;
        cin >> s;
        int steps = 0;
        int curP = s.size() - 1;
        int curC = s[curP];
        if (curC == '-')
            steps++;
        while (curP >= 0) {
            if (s[curP] == curC) {
                curP--;
            } else {
                steps++;
                if (curC == '+') {
                    curC = '-';
                } else {
                    curC = '+';
                }
            }
        }
        results.push_back(steps);
    }
    for (int i = 1; i <= T; i++) {
        cout << "Case #" << i << ": " << results[i - 1] << endl;
    }
    return 0;
}