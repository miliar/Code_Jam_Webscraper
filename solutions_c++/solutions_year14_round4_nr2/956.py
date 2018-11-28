#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n;
    vector<int> a(n);
    vector<int> u(n);
    for(int i = 0; i < n; i++){
        cin >> a[i];
        u[i] = 0;
    }

    int ans = 0;
    int l = 0, r = n-1;

    for(int i = 0; i < n; i++){
        int m = INT_MAX/2;
        int id;
        for(int j = 0; j < n; j++){
            if(u[j]) continue;
            if(m > a[j]){
                m = a[j]; id = j;
            }
        }
        u[id] = 1;

        int lc = 0, rc = 0;
        for(int j = 0; j < n; j++){
            if(u[j]) continue;
            if(j < id) lc++;
            if(j > id) rc++;
        }
        ans += min(lc,rc);
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
    return 0;
}
