#include <bits/stdc++.h>
using namespace std;

int main(){
    int t, cases = 1;
    cin >> t;
    while (t--){
        string s;
        cin >> s;

        string ans;
        ans = s[0];
        for (int i = 1; i < s.length(); i++){
            string first;
            first = s[i];
            first += ans;
            string second = ans + s[i];
            if (first > second) ans = first;
            else ans = second;
        }

        cout << "Case #" << cases++ << ": " << ans << endl;
    }
    return 0;
}
