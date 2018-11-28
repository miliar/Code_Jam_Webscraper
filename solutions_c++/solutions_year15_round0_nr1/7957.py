#include <iostream>
#include <string>

using namespace std;

int solve(int s_max, string s) {
    int friends = 0;
    int audience = 0;
    for (int i = 0; i <= s_max; ++i) {
        if (audience < i) {
            friends += i - audience;
            audience = i;
        }
        audience += s[i] - '0';
    }
    return friends;
}

int main() {
    int t;
    cin >> t;
    for (int case_num = 1; case_num <= t; ++case_num) {
        int s_max;
        string s;
        cin >> s_max;
        cin >> s;
        cout << "Case #" << case_num << ": " << solve(s_max, s) << endl;
    }
    return 0;
}
