#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n,x;
    cin >> n >> x;
    vector<int> s(n);
    for(int i = 0; i < n; i++){
        cin >> s[i];
    }

    sort(begin(s),end(s));
    int l = 0, r = n-1;
    int ans = 0;
    while(l <= r){
        if(l == r){
            ans++;
            l++; r--;
        } else if(s[l]+s[r] <= x){
            ans++;
            l++; r--;
        } else {
            ans++;
            r--;
        }
    }
    cout << ans << endl;
}

int main(){
    int T;
    cin >> T;
    for(int i = 1; i <= T; i++){
        printf("Case #%d: ", i);
        solve();
    }
}
