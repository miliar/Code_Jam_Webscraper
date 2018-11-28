#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cassert>
using namespace std;

string s;
int n;

int solve() {
    int res = 0;
    for (int i = 0; i < s.length(); i++) {
        int j = i;
        int k = n;
        for (; k != 0 && j < s.length(); j++)
            if (s[j] != 'a'
             && s[j] != 'e'
             && s[j] != 'i'
             && s[j] != 'o'
             && s[j] != 'u')
                k--;
            else
                k = n;
        if (k != 0)
            continue;
        res += s.length() - j + 1;
    }
    return res;
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cout << "Case #" << i << ": ";
        cin >> s >> n;
        cout << solve();
        cout << "\n";
    }
    return 0;
}
