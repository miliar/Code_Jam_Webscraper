#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    long long t ;
    freopen("in.txt", "rt", stdin);
    freopen("out.txt", "wt", stdout);
    cin >> t ;
    for (int i = 1 ; i <= t ; i++ )
    {
        string s;
        cin >> s;
        int sz = int(s.size()) , c = 0;
        s += '+';
        for (int idx = 0; idx < sz ; idx++ )
        {
            if (s[idx] != '+' && s[idx] != s[idx + 1])
                c ++;
        }
        cout << "Case #" << i << ": " << c * 2 - (s[0] == '-')<< endl;
    }
}
