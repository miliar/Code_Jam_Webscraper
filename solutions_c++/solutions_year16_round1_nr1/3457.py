#include <bits/stdc++.h>

using namespace std;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("ALarge.out","w",stdout);
    int T;
    cin >> T;
    string s;
    set<string> visit;
    for(int cases=1; cases<=T; cases++){
        cin >> s;
        string ans = string(1,s[0]);
        for(int i=1; i<s.size(); i++){
            if( ans[0] <= s[i] ){
                ans = s[i] + ans;
            }else{
                ans.push_back( s[i] );
            }
        }
        cout << "Case #" << cases << ": " << ans << endl;
    }
}
