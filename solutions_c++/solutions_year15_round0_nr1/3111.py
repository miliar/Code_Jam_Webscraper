#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <memory.h>
#include <algorithm>
#include <vector>

#define DB(x) cerr << #x << ": " << x << endl;

using namespace std;

const char* inputFile = "A-large.in";
const char* outputFile = "A-large.out";

class Solver {
public:
    Solver() {
    }

    string solveTest() {
        int sMax;
        string counts;
        cin >> sMax >> counts;
        int have = 0;
        int need = 0;
        for (int i = 0; i <= sMax; ++i) {
            int count = counts[i] - '0';
            if ((count > 0) && (have < i)) {
                int add = i - have;
                need += add;
                have += add;
            }
            have += count;
        }
        return std::to_string(need);
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
