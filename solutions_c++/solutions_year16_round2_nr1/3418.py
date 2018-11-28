#include <bits/stdc++.h>
using namespace std;

string p[10] = {"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
unordered_map<string, string> ans;

void pre(string a, string b) {
    if (a.length()>20) {
        return;
    }
    //cerr<<a<<" "<<b<<" "<<endl;
    sort(a.begin(), a.end());
    ans[a] = b;
    for(int i=0 ; i< 10 ; i++) {
        string y = b;
        y+=('0'+i);
        pre(a+p[i], y);
    }
}

void solve() {
    string s;
    cin>>s;
    sort(s.begin(), s.end());
    s=ans[s];
    sort(s.begin(), s.end());
    cout<<s<<endl;
}

int main(int argc, const char **argv) {
    if(argc>=2) {
        freopen(argv[1], "r", stdin);
        freopen(argv[2], "w", stdout);
    }
    pre("", "");
    cerr<<"DONE"<<" "<<endl;

    int T;
    cin>>T;
    for(int t=1 ; t<=T ; t++) {
        printf("Case #%d: ",t);
        solve();
    }
}
