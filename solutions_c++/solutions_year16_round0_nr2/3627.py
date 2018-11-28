#include <iostream>
#include<unordered_set>

using namespace std;

int flip(string & s) {
    if (s.empty()) {
        return 0;
    }
    int res = s.back() == '+' ? 0 : 1;
    for (int i = 1; i < s.size(); ++i) {
        if (s[i] != s[i - 1]) {
            ++res;
        }
    }
    return res;
}


int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        string s;
        cin >> s;
        cout << "Case #" << i << ": " << flip(s) << "\n";
    }

    return 0;
}