#include <bits/stdc++.h>

using namespace std;

int main()
{
    int T,t;
    cin >> T;
    for(t=1;t<=T;++t)
    {
        string s;
        cin >> s;
        while(s.size() && s[s.size()-1]=='+') s = s.substr(0,s.size()-1);
        int f = (s.size()>0);
        for(int i=1;i<s.size();++i) f += (s[i]!=s[i-1]);
        cout << "Case #" << t << ": " << f << "\n";
    }
    return 0;
}
