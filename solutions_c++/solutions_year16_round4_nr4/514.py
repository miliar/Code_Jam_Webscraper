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
const char* inputFile = "D-small-attempt0.in";
const char* outputFile = "D-small-attempt0.out";
//const char* inputFile = "A-large.in";
//const char* outputFile = "A-large.out";

const int INF = 1e9;

bool bit(int mask, int b)
{
    return (mask & (1ll << b)) > 0;
}

class Solver {
public:
    Solver() {
    }

    string solveTest() {
        int n;
        cin >> n;
        vector<vector<char>> can(n);
        REP(i, n) {
            string s;
            cin >> s;
            can[i].resize(n);
            REP(j, n) {
                can[i][j] = s[j] == '1';
            }
        }

        int edges = n * n;
        int minCost = edges;
        for (int mask = 0; mask < (1ll << edges); ++mask) 
        {
            auto newCan = can;
            bool bad = false;
            int cost = 0;
            REP(i, edges) {
                if (bit(mask, i)) {
                    int s = i / n;
                    int f = i % n;
                    if (newCan[s][f]) {
                        bad = true;
                        break;
                    }
                    newCan[s][f] = true;
                    ++cost;
                }
            }
            if (bad) {
                continue;
            }

            if (unorderedCheck(newCan)) {
                if (cost < minCost) {
                    minCost = cost;
                }
            }
        }
        return to_string(minCost);
    }

    bool unorderedCheck(const vector<vector<char>>& can)
    {
        vector<int> perm;
        REP(i, can.size()) {
            perm.push_back(i);
        }

        do
        {
            if (!orderedCheck(can, perm)) {
                return false;
            }
        } while (next_permutation(perm.begin(), perm.end()));
        return true;
    }

    bool orderedCheck(const vector<vector<char>>& can, const vector<int>& order)
    {
        vector<char> used(can.size(), false);
        return dfsCheck(can, order, 0, used);
    }

    bool dfsCheck(const vector<vector<char>>& can, const vector<int>& order, int cur, vector<char>& used)
    {
        if (cur == can.size()) {
            return true;
        }

        int id = order[cur];
        bool canFill = true;
        int ways = 0;
        for (int i = 0; i < can[id].size(); ++i) {
            if (can[id][i] && !used[i]) {
                ++ways;
                used[i] = true;
                canFill &= dfsCheck(can, order, cur + 1, used);
                used[i] = false;
            }
        }
        return (canFill && ways > 0);
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
