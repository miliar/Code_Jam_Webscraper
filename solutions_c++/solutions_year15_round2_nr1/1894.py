#include <iostream>
#include <vector>
#include <stdio.h>
#include <algorithm>
#include <sstream>
#include <string>
#include <cstring>

using namespace std;

long long ireverse(long long i){
    long long res = 0;
    if(i%10 == 0) return -1;
    while(i){
        res = res*10 + i%10;
        i /= 10;
    }
    return res;
}

int dp[1000010];

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    memset(dp, 0, sizeof(dp));

    for(int i=1; i<1000010; i++){
        dp[i] = dp[i-1] + 1;
        int ire = ireverse(i);
        if(ire != -1 && ire < i) dp[i] = min(dp[i], dp[ire] + 1);
    }
    int T, test;
    cin >> T;
    for(test=1; test<=T; test++){
//        memset(dp, 0, sizeof(dp));

//        long long N;
//        cin >> N;
//        long long res = 0;
//        for(long long i=1; i<=N; ){
//            res++;
//            long long re = ireverse(i);
//            if(re != -1 && re > i && re <= N) {
//                i = re;
//            }
//            else i++;
//        }
        int N;
        cin >> N;

        printf("Case #%d: %d\n", test, dp[N]);
    }

    return 0;
}
