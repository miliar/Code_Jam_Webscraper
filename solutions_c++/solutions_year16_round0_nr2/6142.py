#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cmath>
using namespace std;

void solve(int t, string s)
{
    int ans = 0;
    int pos = 0;
    while(pos < s.size())
    {
        pos = 0;
        while(pos < s.size() && (pos == 0 || (s[pos] == s[pos - 1]))) ++pos;
        if (pos == s.size() && s[0] == '+') break;
        for (int i = 0; i < pos; ++i)   
            s[i] = (s[i] == '+') ? '-' : '+';
        ++ans;
    }
    cout << "Case #" << t + 1 << ": " << ans << endl;
}

int main()
{
    int t;
    string s;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        cin >> s;   
        solve(i, s);
    }
}
