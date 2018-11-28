#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T, NT;
    cin>>NT;
    for(T=1; T<=NT; ++T) {
        int n;
        cin>>n;
        vector<int> v(n);
        int to = 0;
        for(int i=0; i<n; ++i) {
            cin>>v[i];
            to = max(to, v[i]);
        }
        int res=to;
        for(int i=1; i<=to; ++i) {
            int cur = i;
            int add = 0;
            for(int j=0; j<n; ++j) {
                add += (v[j] + i - 1) / i - 1;
            }
            res = min(res, cur + add);
        }
        cout<<"Case #"<<T<<": "<<res<<endl;
    }
    return 0;
}
