#include<bits/stdc++.h>
using namespace std;
int main()
{
   // freopen("in.in", "r", stdin);
   // freopen("out.out", "w", stdout);
    string s;
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cout << "Case #" << i+1 << ": ";
        cin >> s;
        int sm = 0, n = s.size();
        s+=s[n-1];
        for (int i = 0; i < n; i++)
        {
            if (s[i] == '-')
                sm++;
            while(s[i] == s[i+1] && i < n)
                i++;
        }
        if (sm)
            cout << sm*2-(s[0]=='-');
        else
            cout << '0';
        cout << '\n';
    }
}
