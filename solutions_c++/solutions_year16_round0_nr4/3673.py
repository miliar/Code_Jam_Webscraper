#include <bits/stdc++.h>
using namespace std;
int main() {
    int tc, k, c, s;
    int cnt = 1;
    cin>>tc;
    while(tc--) {
        cin>>k>>c>>s;
            cout<<"Case #"<<cnt++<<": ";
            for(int i = 1; i <= s; i++) {
                cout<<i<<" ";
            }
            cout<<endl;
        }
    return 0;
}
