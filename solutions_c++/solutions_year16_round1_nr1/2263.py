#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <array>

using namespace std;

string s, r;

string c2s(char c)
{
    string q = "_";
    q[0] = c;
    return q;
}

void solve()
{
    r = "_";
    r[0] = s[0];
    for (int i = 1; i < s.length(); i++) {
        if (s[i] >= r[0]) {
            r = c2s(s[i]) + r;
        } else {
            r = r + c2s(s[i]);
        }
    }
    cout << r << endl;
}

int main()
{
    int t;
    scanf("%d", &t);

    for (int i = 0; i < t; i++) {
        cin >> s;
        printf("Case #%d: ", i + 1);
        solve();
    }
    return 0;
}