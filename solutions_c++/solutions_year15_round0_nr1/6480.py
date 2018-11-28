#include <bits/stdc++.h>

using namespace std;

int main(){
//    freopen("A-large.in","r",stdin);
//    freopen("A_large.out","w",stdout);
    int t;
    cin >> t;
    for(int x=1; x<=t; x++){
        int n; string s;
        cin >> n >> s;
        int prev = s[0]-'0';
        int ans = 0;
        for(int i=1; i<s.size(); i++){
            if( i > prev ){
                ans += i-prev;
                prev += (i-prev);
            }

            prev += s[i]-'0';
        }

        cout << "Case #"<<x<<": " << ans << endl;

    }
}
