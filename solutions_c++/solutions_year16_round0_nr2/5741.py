#include <bits/stdc++.h>

using namespace std;

void solve(int test) {
    printf("Case #%d: ", test);
    string s;
    cin >> s;
    vector<char> sgn;
    for (int i = 0; i < s.length(); i++) {
        int j = i;
        while (j < s.length() && s[j] == s[i]) {
            j++;
        }
        j--;
        sgn.push_back(s[i]);
        i = j;
    }
    int ans;
    if (sgn[0] == '-') {
        ans = sgn.size() - 1 + (sgn.back() == '-');
    }
    else {
        ans = sgn.size() - (sgn.back() == '+');
    }

    cout << ans << endl;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int test;
    cin >> test;
    //test = 1E6;
    for (int i = 1; i <= test; i++) {
        solve(i);
    }
    return 0;
}
