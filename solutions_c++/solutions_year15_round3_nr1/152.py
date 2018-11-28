#include<bits/stdc++.h>

using namespace std;



void solve(){
    int r,c,w;
    cin >> r >>c >> w;
    vector<bool> fire(c,false);
    vector<bool> hit(c,false);
    int ans = c/w;
    int rem=c%w;
    if(ans==1){
        ans=min(c,w+1);
    }
    else   {
        ans+=w;
        if(!rem)ans--;
        if(ans>c)ans=c;
    }
    if(r>1){
        ans+= (r-1)*(c/w);
    }
    cout << ans << endl;

}

int main(){
    freopen("A-large"".in","r",stdin);
    freopen("A-large"".out","w",stdout);
    int T;
    cin >> T;
    for(int i = 1 ; i <= T ; ++ i ){
        cout <<"Case #" <<i <<": ";
        solve();
    }
    return 0;
}
