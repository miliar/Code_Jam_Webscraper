#include <cstdio>
#include <map>
#include <cmath>
#include <iostream>
#include <string>
using namespace std;

int main()
{
    string s;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int test = 1; test <= t; ++test)
    {
        int n, cnt = 0, now = 0;
        cin >> n >> s;
        for (int i = 0; i < s.size(); i++)
        {
            if(s[i] != '0')
            {
                cnt += max(0, i - now);
                now = max(now, i) + s[i] - '0';
            }
        }
        cout << "Case #" << test << ": " << cnt << "\n";
    }
    return 0;
}
