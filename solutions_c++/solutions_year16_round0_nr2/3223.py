#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    int t, ans;
    string s;
    cin >> t;
    for(int c = 1;c <= t;++c)
    {
        cin >> s;
        reverse(s.begin(), s.end());
        ans = 0;
        for(int i = 0;i < s.length();++i)
            if(s[i] == '-')
            {
                ans++;
                for(int j = i;j < s.length();++j)
                    if(s[j] == '-') s[j] = '+';
                    else s[j] = '-';
            }
        cout << "Case #" << c << ": " << ans << endl;
    }
    return 0;
}
