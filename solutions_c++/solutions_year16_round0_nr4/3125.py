#include <bits/stdc++.h>

using namespace std;

int main(){
    freopen("D-small-attempt0.in","r",stdin);
    freopen("DSmall.out","w",stdout);
    int T, k,c,s;
    cin >> T;
    for(int cases=1; cases<=T; cases++){
        cin >> k >> c >> s;
        cout << "Case #" << cases << ": ";
        for(int i=1; i<=k; i++) cout << i << " ";
        cout << endl;
    }
}
