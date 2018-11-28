#include<bits/stdc++.h>
using namespace std;

int main() {
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("d.out", "w", stdout);
    int t, k, c, s;
    cin >> t;
    for(int cs = 1; cs<=t ; cs++) {
        cin >> k >> c >> s;
        cout << "Case #"<<cs<<":";
        for(int i=1;i<=k;i++) cout << " "<<i;cout << endl;
    }
    return 0;
}

