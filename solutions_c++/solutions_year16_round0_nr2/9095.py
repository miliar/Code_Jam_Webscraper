#include <bits/stdc++.h>
using namespace std;

int t;

int main()
{
    //freopen("B-large.in", "r", stdin);
    //freopen("B-large.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> t;
    for(int q = 0; q < t; ++q)
    {
        string s;
        cin >> s;
        int otv = 0;
        if(s[s.size()-1] == '-') otv = 1;
        else otv = 0;
        for(int j = 1; j < s.size(); ++j)
        {
            if(s[j-1] != s[j]) otv++;
        }
        cout << "Case #" << q+1 << ": " << otv << "\n";
    }
}
