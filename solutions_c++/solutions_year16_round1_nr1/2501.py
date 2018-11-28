#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

string s, ans;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int q;
    cin >> q;
    for (int t = 1; t <= q; ++t)
    {
        printf("Case #%d: ", t);
        cin >> s;
        ans.clear();
        ans += s[0];
        for (int i = 1; i < s.length(); ++i)
        {
            if (s[i] >= ans[0])
            {
                ans = s[i] + ans;
            }
            else
            {
                ans = ans + s[i];
            }
        }
        printf("%s\n", ans.c_str());
    }
    return 0;
}