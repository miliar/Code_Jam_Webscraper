#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int caseNum = 1; caseNum <= T; ++caseNum) {
        int sMax;
        string s;
        cin >> sMax >> s;
        vector<int> shy;
        for (char c : s) shy.push_back(c-'0');
        int tot = shy[0], add = 0;
        for (size_t index = 1; index < shy.size(); ++index) {
            if (shy[index]) {
                if (index > tot) {
                    int diff = index - tot;
                    add += diff;
                    tot = index;
                }
                tot += shy[index];
            }
        }
        cout << "Case #" << caseNum << ": " << add << endl;
    }
}
