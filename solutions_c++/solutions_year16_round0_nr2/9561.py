#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int Solve(string s) {
    int cnt = 0;
    for (int i = 0, j; i < s.size(); i = j) {
        for (j = i; j < s.size() && s[i] == s[j]; j++);
        cnt++;
    }
    cnt = cnt - 1 + (s.back() == '-');
    return cnt;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        string n;
        cin >> n;
        cout << "Case #" << i << ": " << Solve(n) << "\n";
    }
}