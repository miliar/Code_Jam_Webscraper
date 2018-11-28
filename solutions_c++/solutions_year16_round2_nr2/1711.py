#include <bits/stdc++.h>
using namespace std;

int match(string x, int z) {
    string y = to_string(z);
    string zero = "0";
    if (y.length()>x.length()) {
        return 0;
    }
    while (x.length()>y.length()) {
        y = zero + y;
    }
    for(int i=0 ; i< x.length() ; i++) {
        if (x[i]=='?') {
            continue;
        }
        if (x[i]!=y[i]) {
            return 0;
        }
    }
    return 1;
}

void solve() {
    string a, b;
    cin>>a>>b;
    int l1,l2,diff = 1e9;
    for(int i=0 ; i< 1000 ; i++) {
        if (!match(a, i)) {
            continue;
        }
        for(int j=0 ; j< 1000 ; j++) {
            if (!match(b, j)) {
                continue;
            }
            if(abs(i-j)<diff) {
                l1 = i;
                l2 = j;
                diff = abs(i-j);
            }
        }
    }
    string x = to_string(l1);
    string zero = "0";
    while (a.length()>x.length()) {
        x = zero + x;
    }
    cout<<x<<" ";
    
    x = to_string(l2);
    while (a.length()>x.length()) {
        x = zero + x;
    }
    cout<<x<<"\n";
}

int main(int argc, const char **argv) {
    if(argc>=2) {
        freopen(argv[1], "r", stdin);
        freopen(argv[2], "w", stdout);
    }
    int T;
    cin>>T;
    for(int t=1 ; t<=T ; t++) {
        printf("Case #%d: ",t);
        solve();
    }
}
