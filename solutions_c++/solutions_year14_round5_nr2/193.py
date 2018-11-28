#include<iostream>
#include<cstring>
using namespace std;
const int BUF = 105;
const int TURN = 1005;
const int LOOP = 20;

int sDmg, tDmg, N, hp[BUF], gold[BUF];

void read() {
    cin >> sDmg >> tDmg >> N;
    for (int i = 0; i < N; ++i) {
        cin >> hp[i] >> gold[i];
    }
}


int rec(int idx, int turn, int dp[BUF][TURN]) {
    if (idx == N) return 0;

    int &ret = dp[idx][turn];
    if (ret != -1) return ret;
    
    ret = 0;
    
    // tower kills
    ret = max(ret, rec(idx + 1, turn + (hp[idx] + tDmg - 1) / tDmg, dp));

    // self kills
    for (int tTurn = 0; tTurn <= LOOP; ++tTurn) {
        if (tTurn * tDmg >= hp[idx]) break;
        for (int sTurn = 1; sTurn <= LOOP; ++sTurn) {
            if (tTurn * tDmg + sTurn * sDmg < hp[idx])
                continue;
            if (turn + tTurn - sTurn < 0)
                break;
            ret = max(ret, rec(idx + 1, turn + tTurn - sTurn, dp) + gold[idx]);
        }
    }

    return ret;
}

void work(int cases) {
    int dp[BUF][TURN];
    memset(dp, -1, sizeof(dp));
    cout << "Case #" << cases << ": " << rec(0, 1, dp) << endl;
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
