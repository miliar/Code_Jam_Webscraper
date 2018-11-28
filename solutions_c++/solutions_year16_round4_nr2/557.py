#include<iostream>
#include<algorithm>
#include<vector>
#include<cstdio>
#include<cstring>
using namespace std;
const int BUF = 205;


int nPpl, nChoose;
double p[BUF];

void read() {
    cin >> nPpl >> nChoose;
    for (int i = 0; i < nPpl; ++i) {
        cin >> p[i];
    }
}


double calc(vector<int> &ids) {
    // dp[idx][nYes] := possibility of nYes
    static double dp[BUF][BUF];
    memset(dp, 0, sizeof(dp));
    dp[0][0] = 1;
    
    for (int idx = 0; idx < nChoose; ++idx) {
        for (int nYes = 0; nYes <= nChoose / 2; ++nYes) {

            // answered yes
            if (nYes + 1 <= nChoose / 2) {
                dp[idx + 1][nYes + 1] += dp[idx][nYes] * p[ids[idx]];
            }
            
            // answered no
            dp[idx + 1][nYes] += dp[idx][nYes] * (1 - p[ids[idx]]);
        }
    }

    return dp[nChoose][nChoose / 2];
}


void work(int cases) {
    sort(p, p + nPpl);
    
    double ans = 0;
    
    for (int nChooseFrmLeft = 0; nChooseFrmLeft <= nChoose; ++nChooseFrmLeft) {
        int nChooseFrmRight = nChoose - nChooseFrmLeft;
        vector<int> ids;
        for (int i = 0; i < nChooseFrmLeft; ++i) ids.push_back(i);
        for (int i = 0; i < nChooseFrmRight; ++i) ids.push_back(nPpl - i - 1);
        ans = max(ans, calc(ids));
    }
    
    printf("Case #%d: %.10lf\n", cases, ans);
}


int main() {
    int cases;
    cin >> cases;
    
    for (int i = 0; i < cases; ++i) {
        read();
        work(i + 1);
    }
    return 0;
}
