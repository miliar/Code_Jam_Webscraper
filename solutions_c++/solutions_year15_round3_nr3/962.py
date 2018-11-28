#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <cstdio>
#include <stack>
#include <list>
#include <cstring>
#include <fstream>
using namespace std;

#define FOR(i,s,e) for (int i = int(s); i < int(e); i++)
#define FORIT(i,c) for (typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define ISEQ(c) (c).begin(), (c).end()
#define REP(i,e) for (int i = 0; i < int(e); ++i)
#define MAX(a,b) ((a) > (b) ? (a):(b))
#define MIN(a,b) ((a) < (b) ? (a):(b))
#define SQR(a) ((a)*(a))

const char probname = 'C';
const bool largeset = false;
const char* suffix = "-attempt2"; //-attempt0

int main() {
    char buffer[1234];
    sprintf(buffer, "%c-%s%s.in", probname, largeset ? "large" : "small", suffix);
    ifstream fin(buffer);
    sprintf(buffer, "%c-%s%s.out", probname, largeset ? "large" : "small", suffix);
    ofstream fout(buffer);

    int testCases;
    fin >> testCases;



    int c, d, v;

    REP(testCase, testCases) {
        fin >> c >> d >> v;

        if (c != 1) continue;

        std::vector <int> coins(d);

        REP(i, d) fin >> coins[i];
        sort(coins.begin(), coins.end());
        std::vector <bool> sums(v + 1, false);
        sums[0] = true;



        REP(i, coins.size()) {
            for (int j = v; j >= 0; --j) {
                if (sums[j] && j + coins[i] <= v) sums[j + coins[i]] = true;
            }
        }

        int res = 0;
        REP(k, v + 1) {
            if (!sums[k]) {
                res++;
                for (int j = v; j >= 0; --j) {
                    if (sums[j] && j + k <= v) sums[j + k] = true;
                }
            }
        }




        fout << "Case #" << testCase + 1 << ": " << res << endl;
        cout << "Case #" << testCase + 1 << ": " << res << endl;
    }

    fin.close();
    fout.close();
}
