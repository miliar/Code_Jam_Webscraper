#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("Aout1.out","w",stdout);
    int t;
    cin >> t;
    for(int IN=0; IN<t; ++IN){
        string s;
        cin >> s;
        deque<char>ans;
        ans.push_back(s[0]);
        for(int i=1; i<s.size(); ++i){
            if(ans[0] <= s[i]) ans.push_front(s[i]);
            else ans.push_back(s[i]);
        }
        cout << "Case #" << IN+1 <<": ";
        for(int i=0; i<s.size(); ++i)
            cout << ans[i];
        cout << endl;
    }
}
