#include <iostream>
using namespace std;

string removeTrailing(string s) {
    int at = s.size();
    while (at - 1 >= 0 && s[at - 1] == '+') {
        at--;
    }
    return s.substr(0, at);
}

int value(string s) {
    string trimmed = removeTrailing(s);
    int count = trimmed[trimmed.size() - 1] == '-';
    for (int i = 1; i < trimmed.size(); i++) {
        count += trimmed[i] != trimmed[i - 1];
    }
    return count;
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        string s;
        cin >> s;
        int val = value(s);
        printf("Case #%d: %d\n", t + 1, val);
    }
    return 0;
}
