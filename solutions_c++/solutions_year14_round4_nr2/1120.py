#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    int t;
    cin>>t;
    for(int tt = 1; tt <= t; ++tt) {
        cout<<"Case #"<<tt<<": ";
        int n;
        cin>>n;
        vector<int> v(n);
        unordered_map<int, int> pos;
        for(int i = 0; i < n; ++i) {
            cin>>v[i];
            pos[v[i]] = i;
        }
        vector<int> vv = v;
        sort(v.begin(), v.end());
        int ans = 1e9;
        do {
            int q = 0;
            int lol = 0;
            unordered_map<int, int> mp;
            for(int i = 0; i < n-1; ++i) {
                if(lol == 0 && v[i] > v[i+1]) {
                    lol = 1;
                }
                else if(lol == 1 && v[i] < v[i+1]) {
                    goto ohi;
                }
            }
            for(int i = 0; i < n; ++i) {
                mp[v[i]] = i;
            }
            for(int i = 0; i < n; ++i) {
                for(int j = 0; j < i; ++j) {
                    if(mp[vv[j]] > mp[vv[i]]) ++q;
                }
            }
            ans = min(ans, q);
            ohi:;
        } while(next_permutation(v.begin(), v.end()));
        cout<<ans<<'\n';
    }
}
