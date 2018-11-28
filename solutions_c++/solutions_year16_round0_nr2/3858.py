#include <iostream>
using namespace std;
void flip(int x, string & s) {
    for(int i = 0; 2*i < x; ++i) {
        swap(s[i], s[x-i-1]);
    }
}
int main() {
    int t;
    cin>>t;
    for(int xx = 0; xx < t; ++xx) {
        cout<<"Case #"<<xx+1<<": ";
        string s;
        cin>>s;
        int ans = 0;
        for(int i = 0; i+1 < s.size(); ++i) {
            if(s[i] != s[i+1]) ++ans;
        }
        if(s.back() =='-') ++ans;
        cout<<ans<<'\n';
    }
}
