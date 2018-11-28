#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    cin >> T;
    for (int t=1;t<=T;t++)
    {
        string s;
        cin >> s;
        int res = 1;
        for (int i=1;i<s.length();i++)
        {
            if (s[i]!=s[i-1])
            {
                res++ ;
            }
        }
        if (s[s.length()-1]=='+')
            res-- ;
        cout << "Case #"<<t <<": "<<res << endl ;
    }
    return 0;
}
