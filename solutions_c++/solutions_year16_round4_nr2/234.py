#include <iostream>
#include <cstring>
#include <iomanip>
#include <vector>
#include <algorithm>

typedef long double ld;
using namespace std;
ld dp[222][222] = {0};
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int tt;
    cin>>tt;
    for(int xx = 0; xx < tt; ++xx) {
        cout<<"Case #"<<xx+1<<": ";
        vector<ld> v;
        int n,k;
        cin>>n>>k;
        for(int i = 0; i < n; ++i) {
            ld q;
            cin>>q;
            v.push_back(q);
        }
        sort(v.begin(), v.end());
        ld ans = 0;
        for(int i = 0; i < n; ++i) {
            for(int j = i; j <= n; ++j) {
                memset(dp, 0, sizeof dp);
                vector<ld> v2;
                //cout<<i<<' '<<j<<'\n';
                for(int k = 0; k < n; ++k) {
                    if(k < i || k >= j) {
                        v2.push_back(v[k]);
                        //cout<<v[k]<<' ';
                    }
                }
                //cout<<'\n';
                if(v2.size() != k) continue;
                dp[0][0] = 1;
                for(int k = 0; k < v2.size(); ++k) {
                    for(int l = 0; l <= n; ++l) {
                        //cout<<v2[k]<<' ';
                        if(l == 0) {
                            dp[k+1][l] = max(dp[k+1][l], dp[k][l]*(1-v2[k]));
                        }
                        else {
                            dp[k+1][l] = max(dp[k+1][l], dp[k][l]*(1-v2[k])+dp[k][l-1]*v2[k]);
                        }
                        //cout<<dp[k+1][l]<<' ';
                    }
                    //cout<<'\n';
                }
                //cout<<v2.size()<<' '<<k/2<<'\n';
                ans = max(ans, dp[v2.size()][k/2]);
            }
        }
        cout<<fixed<<setprecision(15)<<ans<<endl;
    }
}
