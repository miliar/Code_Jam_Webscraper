#include <bits/stdc++.h>

using namespace std;

typedef long long ll;


int main() {

    ll t, n, m, i, j, k, a, b, x;
    cin>>t;
    ll T = t;
    while(t--) {
        cin>>n;
        vector<ll> temp(n, 0);
        vector<vector<ll> > v;
        vector<ll> val(2501, 0);
        for (i=0; i<(2*n-1); i++) {
            v.push_back(temp);
            for (j=0; j<n; j++) {
                cin>>v[i][j];
                val[v[i][j]]++;
            }
        }
        vector<ll> ans;
        for (i=0; i<2501; i++) {
            if (val[i]%2==1) {
                ans.push_back(i);
            }
        }
        sort(ans.begin(), ans.end());
        cout<<"Case #"<<(T-t)<<":";
        for (i=0; i<ans.size(); i++) {
            cout<<" "<<ans[i];
        }
        cout<<endl;
        
    }


    return 0;

}