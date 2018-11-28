#include<bits/stdc++.h>

using namespace std;


void solve(){
    int n;
    cin >> n;
    vector<int> v(n);
    for(int i = 0 ; i < n ; ++ i )cin >> v[i];
    int ans = 10000;
    for(int mx = 1 ; mx <=1000 ; ++ mx ){
        int used = 0;
        for(int i = 0  ; i < n ; ++ i ){
            if(v[i]>mx){
                int g = ( v[i]+mx-1 )/mx;
                used +=g-1;
            }
        }
        ans=min(ans,used+mx);
    }
    cout << ans << endl;
}

int main(){
    freopen("B-large"".in","r",stdin);
    freopen("B-large"".out","w",stdout);
    int t;
    cin >> t;
    for(int i = 1 ; i <= t ; ++ i ){
        printf("Case #%d: ",i);
        solve();
    }
    return 0;
}
