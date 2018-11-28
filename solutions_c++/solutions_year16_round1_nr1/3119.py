#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int test = 1; test <= t; test++){
        string s, ans;
        cin>>s;
        ans += s[0];
        for(int i = 1; i < s.length(); i++){
            if(s[i] >= s[0]){
                ans = s[i] + ans;
                s[0] = s[i];
            }
            else
                ans = ans + s[i];
        }
        cout<<"Case #"<<test<<": "<<ans<<endl;
    }
}