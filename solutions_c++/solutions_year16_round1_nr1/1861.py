#include <bits/stdc++.h>
using namespace std;

int main(){
    std::ios::sync_with_stdio(false);
    freopen("A-large.in","r",stdin);
    freopen("lolzano.out","w",stdout);
    int n; cin >> n;
    for( int i = 1 ; i <= n ; ++i ){
        string cad; cin >> cad;
        string ans = "";
        ans += cad[0];
        for( int j = 1 ; j < (int)cad.size() ; ++j ){
            if( cad[j] < ans[0] ){
                ans = ans + cad[j];
            } else ans = cad[j] + ans;
        }
        cout << "Case #"<<i<<": "<<ans << '\n';

    }

}
