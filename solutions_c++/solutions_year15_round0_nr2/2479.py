#include <iostream>
#include <vector>
using namespace std;
int main() {
    int t;
    cin>>t;
    for(int xx = 1; xx <= t; ++xx) {
        cout<<"Case #"<<xx<<": ";
        int d;
        cin>>d;
        vector<int> v(d);
        for(int i = 0; i < d; ++i) {
            cin>>v[i];
        }
        int ans = 1e5;
        for(int i = 1; i < 1010; ++i) {
            int lol = 0;

            for(int j = 0; j < d; ++j) {
                lol += max(0, v[j] / i + !!(v[j]%i)-1);
            }
            ans = min(ans, lol+ i);
        }
        cout<<ans<<'\n';
    }
}
