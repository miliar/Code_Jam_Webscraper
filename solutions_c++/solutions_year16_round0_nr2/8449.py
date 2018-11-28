#include <bits/stdc++.h>

using namespace std;

#define openfile {freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);}
#define debug 01

string s;
int t;

void solve() {
    int i=s.length()-1;
    while (s[i]=='+') i--;
    int res=0;
    while (i>=0) {
        res++;
        while (i>=0 && s[i]=='-') i--;
        if (i>=0) res++;
        while (i>=0 && s[i]=='+') i--;
    }
    cout<<res<<endl;
}

int main() {
    openfile;
    cin>>t;
    for (int i=1; i<=t; i++) {
        cin>>s;
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
