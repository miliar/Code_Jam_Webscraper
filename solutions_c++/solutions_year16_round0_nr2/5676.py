#include <bits/stdc++.h>
using namespace std;

int main(){
    int t, cases = 1;
    cin >> t;
    while (t--){
        string s;
        cin >> s;

        int ans = 0;
        bool ch = false;

        for (int i = s.length()-1; i >= 0; i--){
            if (ch ^ (s[i] == '-')){
                ans++;
                ch = !ch;
            }
        }

        cout << "Case #" << cases++ << ": " << ans << endl;
    }
    return 0;
}
