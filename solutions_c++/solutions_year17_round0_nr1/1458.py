#include <bits/stdc++.h>
#include <stdio.h>
#include <stdlib.h>
#define int long long
using namespace std;

const int nmax = 100010;

string s;
int k, t, it=0;

void solve(string s, int k){
    int ans=0;
        while (1){
            int pos = s.find('-');
            if (pos>=s.size()) break;
            if (pos+k-1>=s.size()) {
                cout << "Case #" << it << ": IMPOSSIBLE\n";
                return;
            }
            for (int i=pos; i<=pos+k-1; i++) s[i]=(s[i]=='+'?'-':'+');
            ans++;
        }
    cout << "Case #" << it << ": " << ans << endl;
}

main(){
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
    cin >> t;
    while (t--){
    it++;
        cin >> s >> k;
        solve(s, k);
    }

}
