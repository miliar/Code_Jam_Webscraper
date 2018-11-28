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
        string S;
        cin >> S;
        int ans = 0;
        bool onMinus = false;
        bool onPlus = false;
        REP(i, S.length()) {
            if (S[i] == '-') {
                if (!onMinus) {
                    ++ans;
                    if (onPlus) {
                        ++ans;
                        onPlus = false;
                    }
                    onMinus = true;
                }
            } else {
                onPlus = true;
                onMinus = false;
            }
        }
        return to_string(ans);
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
