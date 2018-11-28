#include <iostream>
#include <set>
#include <cstdio>
using namespace std;
int main() {
    //freopen("A-small-attempt0.in","r",stdin);
  //  freopen("output.txt","w", stdout);
    int T;
    cin>>T;
    int k = 0;
    while(T--) {
        string s;
        cin>>s;
        int dp[1000][2];
        dp[0][0] = (s[0] == '+');
        dp[0][1] = (s[0] == '-');
        for(int i = 1; i < s.size(); ++i) {
            if(s[i] == '-') {
                dp[i][0] = dp[i-1][0];
                dp[i][1] = dp[i-1][0] +1;
                dp[i][0] = min(dp[i][0], dp[i-1][1]+2);
                dp[i][1] = min(dp[i][1], dp[i-1][1] + 3);
            }
            else{
                dp[i][1] = dp[i-1][1];
                dp[i][0] = dp[i-1][1] +1;
                dp[i][1] = min(dp[i][1], dp[i-1][0]+2);
                dp[i][0] = min(dp[i][0], dp[i-1][0] + 3);
            }
        }
        printf("Case #%d: %d\n", (++k), min(dp[s.size()-1][1],dp[s.size()-1][0]+1));
    }
    return 0;
}