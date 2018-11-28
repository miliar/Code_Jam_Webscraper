#include <iostream>
#include <cstdio>
using namespace std;

const int maxn = 110;
int T , dp[maxn];
string S;

int main(){
    //freopen("B-large.in" , "r" , stdin);
    //freopen("B-large.out" , "w" , stdout);
    cin >> T;
    for(int t = 1; t <= T; t++){
        cin >> S;
        S = "+"+S;
        for(int i = 0; i < maxn; i++) dp[i] = 0;
        for(int i = 1; i < S.length(); i++){
            if(S[i] == '+' || (S[i] == '-' && S[i-1] == '-')) dp[i] = dp[i-1];
            else{
                dp[i] = dp[i-1]+2;
                if(i == 1) dp[i]--;
            }
        }
        printf("Case #%d: %d\n" , t , dp[S.length()-1]);
    }
    return 0;
}
