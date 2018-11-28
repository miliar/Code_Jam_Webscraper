#include <iostream>
#include <cstdio>

using namespace std;

int main() {
    freopen("./large.in", "r", stdin);
    freopen("./large.out", "w", stdout);

    int t;
    cin >> t;

    for (int i=1; i<=t; ++i) {
        string input;
        cin >> input;
        string ans = input.substr(0,1);
        string front = ans, back = ans;
        for (int j=1; j<input.length(); ++j) {
            string temp = input.substr(j,1);
            if (temp >= front) {
                ans = temp + ans;
                front = temp;
            }
            else {
                ans = ans + temp;
            }
        }
        cout << "Case #" << i << ": " << ans << "\n";
    }
}
