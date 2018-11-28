#include <bits/stdc++.h>

using namespace std;

bool khe(string &curr){
    bool goal = true;
    for(int i=0; i<curr.size() && goal; i++)
        goal = (curr[i] == '+');

    return goal;
}

int main(){
    freopen("B-large.in","r",stdin);
    freopen("BLarge.out","w",stdout);
    int T;
    string s;
    cin >> T;

    for(int cases=1; cases<=T; cases++){
        cin >> s;
        int ans = 0;
        while( !khe(s) ){
            char c = s[0];
            int i = 1;
            while( s[i] == c ) i++;
            for(int j=0; j<i; j++)
                s[j] = (s[j] == '-' ? '+' : '-');
            ans++;
        }

        cout << "Case #" << cases << ": " << ans << endl;
    }
}
