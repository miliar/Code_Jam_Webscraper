#include <iostream>
#include <vector>
#include <stdio.h>
#include <algorithm>
#include <sstream>
#include <string>
#include <cstring>
#include <cmath>

using namespace std;

//int dp[21][21][21][21][21];
int dp[21][21];

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    memset(dp, 0, sizeof(dp));

    for(int k=1; k<=20; k++){
        for(int w=k; w<=20; w++){
            if(w == k) {
                dp[w][k] = k;
                continue;
            }

            if(w-k < k){
                dp[w][k] = k+1;
            }
            else{
                dp[w][k] = max(k+1, dp[w-k][k] + 1);
            }

        }
    }


    for(int test=1; test<=T; test++){
        int C, R, W;
        cin >> R >> C >> W;
        printf("Case #%d: %d\n", test, R*dp[C][W]);
    }
    return 0;

}
