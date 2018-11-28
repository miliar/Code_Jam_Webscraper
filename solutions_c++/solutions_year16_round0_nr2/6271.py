#include <iostream>
#include <vector>
#include <map>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
#define ll long long
int T,ans;
string cake;
void solve(string s)
{
    ans = 0;
    if (s.empty())
        return;
    else
    {
        if (s[0] == '-')
            ans = 1;
        for (int i = 1; i < s.size(); ++i)
            if (s[i] == '-' && s[i-1] == '+')
                ans += 2;
    }
}

int main()
{
    cin >> T;
    for (int i = 1; i <= T; ++i)
    {
        cin >> cake;
        solve(cake);
        printf("Case #%d: %d\n", i, ans);
    }
}
