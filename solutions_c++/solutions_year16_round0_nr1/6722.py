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

using namespace std;

//const char* inputFile = "file.in";
//const char* outputFile = "file.out";
//const char* inputFile = "A-small-attempt0.in";
//const char* outputFile = "A-small-attempt0.out";
const char* inputFile = "A-large.in";
const char* outputFile = "A-large.out";

const int INF = 1e9;

class Solver {
public:
    Solver() {
    }

    unordered_set<int> toVisit;

    void visit(long long x) {
        while (x) {
            toVisit.erase(x % 10);
            x /= 10;
        }
    }

    string solveTest() {
        int N;
        cin >> N;
        REP(i, 10) {
            toVisit.insert(i);
        }
        FOR(i, 1, 10000) {
            visit(N * 1ll * i);
            if (toVisit.empty()) {
                return to_string(N * 1ll * i);
            }
        }

        return "INSOMNIA";
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
