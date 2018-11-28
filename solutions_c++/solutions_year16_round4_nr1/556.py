#include<iostream>
#include<algorithm>
#include<map>
using namespace std;


class Data {
public:
    int nr, np, ns;

    Data(int nr, int np, int ns):
        nr(nr), np(np), ns(ns) {}
    
    bool operator< (const Data &opp) const {
        if (nr != opp.nr) return nr < opp.nr;
        if (np != opp.np) return np < opp.np;
        return ns < opp.ns;
    }
};

// (nr, np, ns) := alphabetically smallest order
map<Data, string> dp;

void makeTable() {
    dp[Data(1, 1, 0)] = "PR";
    dp[Data(1, 0, 1)] = "RS";
    dp[Data(0, 1, 1)] = "PS";
    
    for (int i = 2; i < 13; ++i) {
        for (int j = 0; j < 3; ++j) {
            int r1, p1, s1;
            int r2, p2, s2;
            int base = (1 << i) / 3 + 1;
            base = (base + 1) / 2;
            if (i % 2 == 0) {
                if (j == 0) {
                    r1 = base, r2 = base;
                    p1 = base, p2 = base - 1;
                    s1 = base - 1, s2 = base;
                }
                else if (j == 1) {
                    r1 = base, r2 = base - 1;
                    p1 = base, p2 = base;
                    s1 = base - 1, s2 = base;
                }
                else {
                    r1 = base - 1, r2 = base;
                    p1 = base, p2 = base - 1;
                    s1 = base, s2 = base;
                }
            }
            else {
                if (j == 0) {
                    r1 = base - 1, r2 = base - 1;
                    p1 = base, p2 = base - 1;
                    s1 = base - 1, s2 = base;
                }
                else if (j == 1) {
                    r1 = base, r2 = base - 1;
                    p1 = base - 1, p2 = base - 1;
                    s1 = base - 1, s2 = base;
                }
                else {
                    r1 = base - 1, r2 = base;
                    p1 = base, p2 = base - 1;
                    s1 = base - 1, s2 = base - 1;
                }
            }

            dp[Data(r1 + r2, p1 + p2, s1 + s2)] =
                min(dp[Data(r1, p1, s1)] + dp[(Data(r2, p2, s2))],
                    dp[Data(r2, p2, s2)] + dp[(Data(r1, p1, s1))]);
        }
    }
}


int n, nR, nP, nS;

void read() {
    cin >> n >> nR >> nP >> nS;
}


void work(int cases) {
    cout << "Case #" << cases << ": ";
    
    if (min(nR, min(nP, nS)) + 1 != max(nR, max(nP, nS))) {
        cout << "IMPOSSIBLE" << endl;
    }
    else {
        cout << dp[Data(nR, nP, nS)] << endl;
    }
}


int main() {
    makeTable();
    
    int cases;
    cin >> cases;
    
    for (int i = 0; i < cases; ++i) {
        read();
        work(i + 1);
    }
    return 0;
}
