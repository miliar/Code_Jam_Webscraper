#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

unordered_map<string, int> vis;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("b.out", "w", stdout);
    int T;
    cin>>T;
    for (int cas=1; cas<=T; cas++)
    {
        string s;
        cin>>s;
        string t;
        t.push_back(s[0]);
        for (int i=1; i<s.size(); i++)
        {
            if (s[i]==s[i-1]) continue;
            t.push_back(s[i]);
        }

        int ans=0;
        if (t[t.size()-1]=='-') ans = t.size();
        else ans = t.size()-1;
        cout<<"Case #"<<cas<<": "<<ans<<endl;
    }
}
