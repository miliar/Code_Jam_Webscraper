#include<bits/stdc++.h>

using namespace std;

long long t, j, ans;
string s;

main(){
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    cin >> t;
    for (int ii = 0; ii < t; ii++){
        cin >> s;
        j = s.length() - 1;
        while (s[j] == '+' && j > -1) j--;
        if (j < 0) cout << "Case #" << ii + 1 << ": " << 0 << endl;
        else{
            ans = 0;
            for (int i = 1; i <= j + 1; i++){
                if (s[i] != s[i - 1]) ans++;
            }
            cout << "Case #" << ii + 1 << ": " << ans << endl;
        }
    }
}


