#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <memory.h>
#include <algorithm>
#include <vector>
#include <unordered_set>

#define DB(x) cerr << #x << ": " << x << endl;
#define REP(i, n) for(int i = 0; i < n; ++i)
#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define pb push_back
#define mp make_pair
#define fi first
#define se second

using namespace std;

typedef long long LL;
typedef long double LD;

//const char* inputFile = "file.in";
//const char* outputFile = "file.out";
//const char* inputFile = "A-small-attempt1.in";
//const char* outputFile = "A-small-attempt1.out";
const char* inputFile = "A-large.in";
const char* outputFile = "A-large.out";

const int INF = 1e9;

char letter[3] = {'P', 'R', 'S'};
int loserFor[3] = {1, 2, 0};
int winnerFor[3] = {2, 0, 1};

class Solver {
public:
    Solver() {
    }

    int N;
    int C[3];

    string solveTest() {
        int R, P, S;
        cin >> N >> R >> P >> S;
        C[0] = P;
        C[1] = R;
        C[2] = S;

        vector<int> bestSeq;
        for (int win = 0; win < 3; ++win) {
            auto seq = canWin(win);
            if (seq.size() > 0) {
                sortSeq(seq);
                updSeq(bestSeq, seq);
            }
        }

        if (bestSeq.size() == 0) {
            return "IMPOSSIBLE";
        }

        string ans;
        for (int i = 0; i < bestSeq.size(); ++i) {
            ans += letter[bestSeq[i]];
        }
        return ans;
    }

    void updSeq(vector<int>& bestSeq, const vector<int> seq) {
        if (bestSeq.size() == 0) {
            bestSeq = seq;
            return;
        }
        for (int i = 0; i < bestSeq.size(); ++i) {
            if (seq[i] != bestSeq[i]) {
                if (seq[i] < bestSeq[i]) {
                    bestSeq = seq;
                    return;
                } else {
                    return;
                }
            }
        }
    }

    void compSwap(vector<int>& seq, int pos, int step)
    {
        int nextPos = pos + step;
        REP(i, step) {
            if (seq[pos + i] != seq[nextPos + i]) {
                if (seq[pos + i] < seq[nextPos + i]) {
                    return;
                }
                break;
            }
        }

        REP(i, step) {
            swap(seq[pos + i], seq[nextPos + i]);
        }
    }

    void sortSeq(vector<int>& seq)
    {
        for (int step = 1; step < seq.size(); step *= 2) {
            for (int pos = 0; pos + step < seq.size(); pos += 2 * step) {
                compSwap(seq, pos, step);
            }
        }
    }

    vector<int> canWin(int winner)
    {
        vector<int> resC(3);
        REP(i, 3) {
            resC[i] = C[i];
        }

        auto solution = solve(winner, 0, resC);

        REP(i, 3) {
            if (resC[i] < 0) {
                solution = {};
            }
        }
        return solution;
    }

    vector<int> solve(int winner, int round, vector<int>& resC) {
        if (round == N + 1) {
            return {};
        }
        if (round == N) {
            --resC[winner];
            return {winner};
        }
        int loser = loserFor[winner];
        int left = min(loser, winner);
        int right = max(loser, winner);
        auto vLeft = solve(left, round + 1, resC);
        auto vRight = solve(right, round + 1, resC);
        vector<int> result(vLeft.size() + vRight.size());
        REP(i, vLeft.size()) {
            result[i] = vLeft[i];
        }
        REP(i, vRight.size()) {
            result[i + vLeft.size()] = vRight[i];
        }
        return result;
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
