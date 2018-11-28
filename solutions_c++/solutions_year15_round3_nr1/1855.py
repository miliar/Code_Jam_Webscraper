/*
 * =============================================================================
 *
 *       Filename:  Brattleship.cpp
 *
 *    Description:  A
 *
 *        Created:  05/10/2015 05:12:35 AM
 *       Compiler:  gcc/g++
 *
 *         Author:  Lawrence Wu (llwu), llwu@mit.edu
 *   Organization:  Massachusetts Institute of Technology
 *
 * =============================================================================
 */

#include <iostream>
#include <algorithm>
using namespace std;

int dp[21][21][21];

void gen() {
    for(int w = 1; w <= 20; w++)
    for(int h = 20; h >= 0; h--)
    for(int p = 1; p <= 20; p++) {
        if(h >= w) dp[p][h][w] = 0;
        else if(p == 1) dp[p][h][w] = w - h;
        else if(p > 1) {
            dp[p][h][w] = 1234567; 
            for(int i = 1; i < p && i <= w; i++) {
                int maximin = max(dp[i][h+1][w], dp[p-i][h][w]);
                dp[p][h][w] = min(dp[p][h][w],1+maximin); //minimax
            }
        }
    }
}

int solve(int R, int C, int W) {
    return (R-1)*((C-W+1)/W) + dp[C-W+1][0][W];
}

int main() {
    gen();
    int T;
    cin >> T;
    for(int i = 1; i <= T; i++) {
        int R, C, W;
        cin >> R >> C >> W;
        cout << "Case #" << i << ": " << solve(R,C,W) << '\n';
    }
}
