#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <memory.h>
#include <algorithm>
#include <vector>

#define DB(x) cerr << #x << ": " << x << endl;

using namespace std;

//const char* inputFile = "file.in";
//const char* outputFile = "file.out";
//const char* inputFile = "B-small-attempt0.in";
//const char* outputFile = "B-small-attempt0.out";
const char* inputFile = "B-large.in";
const char* outputFile = "B-large.out";

const int INF = 1e9;

class Solver {
public:
    Solver() {
    }

    string solveTest() {
        int D;
        cin >> D;
        vector<int> P(D);
        int pMax = 0;
        for (int i = 0; i < D; ++i) {
            cin >> P[i];
            pMax = max(pMax, P[i]);
        }

        int ans = pMax;
        if (pMax > 0) {
            for (int eats = 1; eats <= pMax; ++eats) {
                int moves = minMoves(eats, P);
                ans = min(ans, eats + moves);
            }
        }

        return std::to_string(ans);
    }

    int minMoves(int eats, vector<int> P) {
        for (int i = 0; i < P.size(); ++i) {
            P[i] -= eats;
        }
        int moves = 0;
        for (int i = 0; i < P.size(); ++i) {
            if (P[i] >= 0) {
                moves += (P[i] + eats - 1) / eats;
            }
        }
        return moves;
    }
};

int main() {
    freopen(inputFile, "r", stdin);
    freopen(outputFile, "w", stdout);
    int T;
    scanf("%d", &T);

    for (int testNumber = 1; testNumber <= T; ++testNumber) {
        Solver solver;
        string verdict = solver.solveTest();
        printf("Case #%d: %s\n", testNumber, verdict.c_str());
    }
    return 0;
}
