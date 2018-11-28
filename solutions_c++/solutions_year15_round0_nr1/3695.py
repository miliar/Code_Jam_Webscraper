#include<bits/stdc++.h>

using namespace std;

//struct _ { ios_base::Init i; _() { cin.sync_with_stdio(0); cin.tie(0); } } _;


int main() {
    int t, n;
    string s;
    
    cin >> t;
    for(int tt = 0; tt < t; ++tt) {
        cin >> n >> s;
        int curr = 0, ans = 0;
        
        for(int i = 0; i < s.size(); ++i) {
            if(i <= curr) { 
                curr += s[i] - '0';
            }
            else {
                ans += (i - curr);
                curr += s[i] - '0' + (i - curr);
            }
        }

        cout << "Case #" << tt + 1 << ": " << ans << endl;
    }
    return 0;
}
