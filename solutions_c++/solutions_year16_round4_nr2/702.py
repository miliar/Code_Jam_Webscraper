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
const char* inputFile = "B-small-attempt0.in";
const char* outputFile = "B-small-attempt0.out";
//const char* inputFile = "A-large.in";
//const char* outputFile = "A-large.out";

const int INF = 1e9;

bool bit(int n, int b)
{
    return n & (1ll << b);
}

class Solver {
public:
    Solver() {
    }

    string solveTest() {
        int n, k;
        cin >> n >> k;
        vector<double> p(n);
        REP(i, n) {
            cin >> p[i];
        }

        double bestP = 0;
        for (int mask = 0; mask < (1ll << n); ++mask) {
            vector<double> taken;
            for (int i = 0; i < n; ++i) {
                if (bit(mask, i)) {
                    taken.push_back(p[i]);
                }
            }
            if (taken.size() == k) {
                double p = pTie(taken);
                if (p > bestP) {
                    bestP = p;
                }
            }
        }
        return to_string(bestP);
    }

    void choiceProb(const vector<double>& p, double prob, int cur, int k, double& sum, bool rev) {
        if (cur == p.size()) {
            if (k == 0) {
                sum += prob;
            }
            return;
        }

        double P = p[cur];
        if (rev) {
            P = 1 - P;
        }
        choiceProb(p, prob * (1 - P), cur + 1, k, sum, rev);
        if (k > 0) {
            choiceProb(p, prob * P, cur + 1, k - 1, sum, rev);
        }
    }

    double pTie(vector<double> p) {
        double sum = 0;
        choiceProb(p, 1.0, 0, p.size() / 2, sum, false);
        return sum;
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
