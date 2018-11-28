#include <bits/stdc++.h>
using namespace std;

void solve() {
    string s;
    cin >>s;
    int ans = 0;
    s+= "+";
    int p = 0;
    for(int i=0 ; i< s.length() ; i++) {
        if (s[i] == '+' && p) {
            ans += 2;
            p = 0;
        }
        if (s[i] == '-') {
            p = 1;
        }
    }
    if (s[0]=='-') {
        ans --;
    }
    cout<<ans<<endl;
}

int main(int argc, const char **argv) {
    assert(freopen("input.txt", "r", stdin));
    assert(freopen("output.txt", "w", stdout));
    int T;
    cin>>T;

    for(int t=1 ; t<=T ; t++) {
        cout<<"Case #"<<t<<": ";

        cerr<<"FINISHED"<<" "<<t<<" "<<endl;
        solve();
    }

}
