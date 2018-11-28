#include<bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n ;
    vector<int> v(n);
    for(int i = 0 ; i < n ; ++ i ){
        cin >> v[i];
    }
    int ans1=0;
    int mxdif=0;
    for(int i = 1 ; i < n ; ++ i ){
        ans1+=max(0,v[i-1]-v[i]);
        mxdif=max(mxdif,v[i-1]-v[i]);
    }
    int ans2=0;
    for(int i = 1 ; i < n ; ++ i ){
        ans2+=min(mxdif,v[i-1]);
    }
    printf("%d %d\n",ans1,ans2);

}

int main(){
    freopen("A-large"".in","r",stdin);
    freopen("A-large"".out","w",stdout);
    int t;
    cin >> t;
    for(int i = 1 ; i <= t ; ++ i ){
        printf("Case #%d: ",i);
        solve();
    }

    return 0;
}
