#include <bits/stdc++.h>

using namespace std;
const int maxn = 1e4;
int dp[2][maxn];
main(){
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    dp[0][1] = 0;
    dp[1][1] = 1;
    /// 0 + first        1 - first
    for(int i=2; i<=1000; i++){
        for(int j=0; j<2; j++){
            if(j == 0){
                if(i & 1) dp[j][i] = dp[j][i-1];
                else dp[j][i] = dp[1 - j][i-1] + 1;
            }
            else{
                if(i % 2 == 0) dp[j][i] = dp[j][i-1];
                else dp[j][i] = dp[1 - j][i - 1] + 1;
            }
        }
    }
    int T;
    cin >> T;
    for(int i=0; i<T; i++){
        cout << "Case #" << i + 1 << ": ";
        string s;
        cin >> s;
        int b = 1;
        for(int i=1; i<s.size(); i++)
            if(s[i] != s[i - 1]) b++;
        if(s[0] == '+') cout << dp[0][b] << endl;
        else cout << dp[1][b] << endl;
    }
}
