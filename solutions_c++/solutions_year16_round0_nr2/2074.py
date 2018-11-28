#include <bits/stdc++.h>
using namespace std;

string s;
int n;

void input()
{
    cin >> s;
    n = s.length();
}

void solve()
{
    int cnt = 0;
    for (int i = 0; i < n-1; ++i) {
        cnt += s[i] != s[i+1];
    }
    if (s[0] == '-') {
        cnt |= 1;
    } else {
        cnt += cnt & 1;
    }
    cout << cnt << endl;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        input();
        cout << "Case #" << i << ": ";
        solve();
    }
}
