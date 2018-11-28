#include <iostream>
using namespace std;
int main() {
    int tt;
    cin>>tt;
    for(int xx = 1; xx <= tt; ++xx) {
        cout<<"Case #"<<xx<<": ";
        int n, l;
        cin>>n>>l;
        string s;
        string b;
        for(int i = 0; i < l; ++i) b.push_back('1');
        int lol = 0;
        for(int i = 0; i < n; ++i) {
            cin>>s;
            if(s == b) {
                lol = 1;
            }
        }
        cin>>b;
        if(lol) {
            cout<<"IMPOSSIBLE\n";
            continue;
        }
        if(l == 1) {
            cout<<"? 0";
            cout<<'\n';
            goto ohi;
        }
        for(int i = 0; i < l-1; ++i) {
            cout<<"1";
        }
        cout<<' ';
        for(int i = 0; i < l; ++i) {
            cout<<"0?";
        }
        cout<<'\n';
        ohi:;
    }
}
