#include <bits/stdc++.h>

using namespace std;

#define INF 1<<30
#define MOD 1000000007
typedef long long ll;

int main(){

    int t; cin >> t;
    int cases = 1;
    while(t--){
        string s, ans = ""; cin >> s;
        for(int i=0; i<(int)s.size(); ++i){
            if(!i) ans += s[i];
            else{
                if(s[i] - '0' >= ans[0] - '0') ans = s[i] + ans;
                else ans = ans + s[i];
            }
        }
        cout << "Case #" << cases++ << ": " << ans << endl;
    }

	return 0;
}
