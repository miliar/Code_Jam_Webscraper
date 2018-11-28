#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <array>

using namespace std;

string s;

void solve()
{
    int ans = 0;
    char last = s[0];
    for (int i = 1; i < s.length(); i++) {
        if (s[i] != last) {
            ans++;
            last = s[i];
        }
    }
    if (last != '+') {
        ans++;
    }
    printf("%d\n", ans);
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