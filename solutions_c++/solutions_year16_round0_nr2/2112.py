#include <bits/stdc++.h>

using namespace std;

int main()
{
    ifstream cin("pancake.in");
    ofstream cout("pancake.out");
    int t; cin >> t;
    for(int q = 0; q < t; q++){
        string s; cin >> s;
        cout << "Case #" << (q+1) << ": ";
        s += '+';
        int ans = 0;
        for(int i = 1;i<s.size();i++){
            if(s[i] != s[i-1])
                ans++;
        }
        cout << ans << "\n";
    }
    return 0;
}
