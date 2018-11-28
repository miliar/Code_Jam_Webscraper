#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

int solve(int l, const vector<int>& s) {
    int result = 0;

    int standed = 0;

    for (int i = 0; i <= s.size(); ++i) {
        if (i == 0) {
            standed += s[i];
            continue;
        }
        if (standed < i) {
            result += i - standed;
            standed = i;
        }
        standed += s[i];
    }

    return result;
}

int main() {
    ifstream ifs("large");
    int t;

    ifs >> t;
    cout << "t: " << t << endl;

    for (int i = 0; i < t; ++i) {
        int l; 
        string str;
        ifs >> l >> str;

        vector<int> s(l + 1);
        for (int ii = 0; ii <= l; ++ii) {
            s[ii] = str[ii] - '0';
        }
        cout << "Case #" << i + 1 << ": " << solve(l, s) << endl;
    }
}
