#include <bits/stdc++.h>

using namespace std;

const int N = 100005;

int n, p, s, r;
string dp[N][3];

void calcDP() {
    dp[0][0] = 'P';
    dp[0][1] = 'S';
    dp[0][2] = 'R';
    for (int i = 1; i <= 12; i++) {
        dp[i][0] = min(dp[i - 1][0] + dp[i - 1][2], dp[i - 1][2] + dp[i - 1][0]);
        dp[i][1] = min(dp[i - 1][1] + dp[i - 1][0], dp[i - 1][0] + dp[i - 1][1]);
        dp[i][2] = min(dp[i - 1][2] + dp[i - 1][1], dp[i - 1][1] + dp[i - 1][2]);
    }
}

bool sumsGood(int k) {
    int sumS = 0, sumP = 0, sumR = 0;
    for (int i = 0; i < dp[n][k].size(); i++) {
        if (dp[n][k][i] == 'S') {
            sumS++;
        }
        if (dp[n][k][i] == 'P') {
            sumP++;
        }
        if (dp[n][k][i] == 'R') {
            sumR++;
        }
    }
    return sumS == s && sumP == p && sumR == r;
}

string printAnswer(int k) {
    return dp[n][k];
}

void testCase() {
    scanf("%d %d %d %d", &n, &r, &p, &s);
    string best = "";
    if (sumsGood(0)) {
        best = printAnswer(0);
    } else if (sumsGood(1)) {
        if (best != "") best = min(best, printAnswer(1));
        else
        best = printAnswer(1);
    } else if (sumsGood(2)) {
        if (best != "") best = min(best, printAnswer(2));
        else
            best = printAnswer(2);
    } else {
        printf("IMPOSSIBLE\n");
        return;
    }
    printf("%s\n", best.c_str());
}

int main() {
    calcDP();
    int tests;
    scanf("%d", &tests);

    for (int t = 1; t <= tests; t++) {
        printf("Case #%d: ", t);
        testCase();
    }

    return 0;
}