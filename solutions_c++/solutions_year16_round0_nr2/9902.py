#include <string>
#include <iostream>

using namespace std;

int solve(string& s) {
    int i = 0;
    int res = 0;

    while (i < s.length() && s[i] == '-') 
        i++;

    if (i != 0) 
        res = 1;

    int f = 0;
    while (i < s.length()) {
        if (s[i] == '-') 
            f = 1;
        else
            if (f) {
                res += 2;
                f = 0;
            }
        i++;
    }

    if (f)
        res += 2;

    return res;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        string s;
        cin >> s;
        cout << "Case #" << t << ": " << solve(s) << endl;
    }

    return 0;
}
