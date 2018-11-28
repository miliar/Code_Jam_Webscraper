#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<memory.h>
#include<map>
#include<string>
using namespace std;


int dp[101][2];

void test_case()
{
    
    memset(dp,-1,sizeof(dp));
    
    string s;
    cin >> s;
    int n = s.length();
    dp[0][0] = dp[0][1] = 0 ;
    if(s[0] == '-'){
        dp[0][1] = 1;
    }else{
        dp[0][0] = 1;
    }
    for(int i = 1 ; i < n ; i ++){
        dp[i][0] = dp[i][1] = 1e9;
        bool is_plus = (s[i] == '+');
        if(s[i] == s[i-1]){
            dp[i][0] = dp[i-1][0];
            dp[i][1] = dp[i-1][1];
        }
        if(is_plus){
            dp[i][1] = min(dp[i][1], dp[i-1][1]);
            dp[i][1] = min(dp[i][1], dp[i-1][0] + 1);
            
            dp[i][0] = min(dp[i][0], dp[i-1][0] + 2);
            dp[i][0] = min(dp[i][0], dp[i-1][1] + 1);
        }else{
            dp[i][1] = min(dp[i][1], dp[i-1][1] + 2);
            dp[i][1] = min(dp[i][1], dp[i-1][0] + 1);
            
            dp[i][0] = min(dp[i][0], dp[i-1][0]);
            dp[i][0] = min(dp[i][0], dp[i-1][1] + 1);
        }
    }
    cout << dp[n-1][1] << endl;
}
int main(){
    freopen("/Users/waps12b/Downloads/B-large.in","r",stdin);
    freopen("/Users/waps12b/Downloads/out.txt","w+",stdout);
    
    int t;
    scanf("%d",&t);
    for(int i = 1; i<= t; i++){
        printf("Case #%d: ", i);
        test_case();
    }
    
    return 0;
}