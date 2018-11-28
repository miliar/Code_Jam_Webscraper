#include <vector>
#include <list>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <string>

#define FOR(i,a,b)  for(int i=(a);i<(b);++i)
#define REP(i,a)    FOR(i,0,a)
#define MP          make_pair
#define PB          push_back
#define ST          first
#define ND          second

using namespace std;

using VI  = vector<int>;
using VVI = vector<VI>;
using PII = pair<int, int>;
using VII = vector<PII>;
using LL  = long long int;
using ULL = unsigned long long int;

int testCases;
int N;

const int MAXN = 105;

string input[MAXN];
string single;
int cnt[MAXN][MAXN];

void solve() {
    cin >> N;
    REP(i, N) {
        cin >> input[i];
    }

    single = "";
    char prev = (char)0;
    REP(i, input[0].length()) {
        if (input[0][i] != prev) {
            single += input[0][i];
            prev = input[0][i];
        }
    }

    REP(i, MAXN)
        REP(j, MAXN)
            cnt[i][j] = 0;

    REP(i, N) {
        int pos = -1;
        prev = (char)0;
        REP(j, input[i].length()) {
            if (input[i][j] != prev) {
                ++pos;
                if (pos >= single.length() || single[pos] != input[i][j]) {
                    cout << "Fegla Won\n";
                    return;
                }
                prev = input[i][j];
            }
            cnt[i][pos] += 1;
        }
        if (pos != single.length() - 1) {
            cout << "Fegla Won\n";
            return;
        }
    }

    int res = 0;
    REP (i, single.length()) {
        vector<int> cnts(N, 0);
        REP(j, N) {
            cnts[j] = cnt[j][i];
        }
        sort(cnts.begin(), cnts.end());
        int med = cnts[cnts.size() / 2];
        REP(j, N) {
            res += abs(med - cnts[j]);
        }
    }

    cout << res << "\n";
}

int main() {
    cin >> testCases;
    for (int i = 1; i <= testCases; ++i) {
        cout << "Case #" << i << ": ";
        solve();
    }
}

