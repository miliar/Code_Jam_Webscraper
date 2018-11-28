#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, NT;
    cin>>NT;
    for(T=1; T<=NT; ++T) {
        int n;
        cin>>n;
        string s;
        cin>>s;
        int cur = 0;
        int res=0;
        for(int i=0; i<n; ++i) {
            cur += s[i]-'0' - 1;
            if (cur < 0) {
                ++res;
                ++cur;
            }
        }
        cout<<"Case #"<<T<<": "<<res<<endl;
    }
    return 0;
}
