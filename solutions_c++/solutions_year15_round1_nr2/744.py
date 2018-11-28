#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ifstream cin("stuff.in");
    ofstream cout("stuff.out");
    
    ll m[1005];
    ll t; cin >> t; for (int i = 0; i < t; ++i) {
        ll b, n; cin >> b >> n; for (int i = 0; i < b; ++i)
            cin >> m[i];
        
        // cout << i << endl;
        ll lo = 0; ll hi = 1e15+5; ll s = 0; while (lo != hi) {
            ll mid = (lo+hi+1)/2; s = 0;
            for (int j = 0; j < b; ++j)
                s += (mid+m[j]-1)/m[j];
            if (s >= n)
                hi = mid-1;
            else
                lo = mid;
            
            // cout << mid << ' ' << s << ' ' << lo << ' ' << hi << endl;
        }
        
        s = 0; for (int j = 0; j < b; ++j)
            s += (lo+m[j]-1)/m[j];
        
        vector<int> p; for (int j = 0; j < b; ++j)
            if (lo%m[j] == 0)
                p.push_back(j+1);
        
        cout << "Case #" << i+1 << ": " << p[n-1-s] << endl;
    }
}