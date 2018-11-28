#include <iostream>
#include <algorithm>
#include <cstring>
#include <set>

using namespace std;

double a[1010], b[1010];

int main() {
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    ios::sync_with_stdio(false);
    int T; cin>>T;
    int cas = 0;
    while(T--) {
        int n; cin>>n;
        for(int i=0; i<n; i++) {
            cin>>b[i];
        }
        for(int i=0; i<n; i++) {
            cin>>a[i];
        }
        sort(a, a+n); sort(b, b+n);
        set<double> s;
        for(int i=0; i<n; i++) s.insert(a[i]);
        int ans2 = 0;
        for(int i=0; i<n; i++) {
            auto it = s.upper_bound(b[i]);
            if(it == s.end()) ++ ans2;
            else s.erase(it);
        }
        int ans1 = 0;
        for(int j=0; j<n; j++) {
            int tmp = 0;
            for(int i=0; i<n; i++) {
                if(b[(i+j)%n] > a[i]) {
                    ++ tmp;
                }
            }
            ans1 = max(ans1, tmp);
        }
        cout<<"Case #"<<++cas<<": "<<ans1<<" "<<ans2<<endl;
    }

    return 0;
}
