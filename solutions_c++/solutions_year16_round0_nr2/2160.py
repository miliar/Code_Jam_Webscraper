#include <iostream>
#include <ctime>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solve(string s) {
    int res = 0;
    if (s[0]=='-')res++;
    while (s.length() > 0 && s[0] == '-') {
        s = s.substr(1);
    }
    if (s.length() == 0)return res;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '-' && s[i - 1] == '+')res+=2;
    }

    return res;

}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tcs;
    cin >> tcs;
    for (int tc = 1; tc <= tcs; tc++) {
        string s;
        cin >> s;
        int res = solve(s);
        reverse(s.begin(), s.end());
        res = min(res, solve(s) + 1);

        cout << "Case #" << tc << ": ";
        cout << res << endl;

    }


    return 0;
}