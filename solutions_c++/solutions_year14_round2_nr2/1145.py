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
int A, B, K;

void solve() {
    cin >> A >> B >> K;
    int res = 0;
    REP(i, A) {
        REP(j, B) {
            if ((i & j) < K) {
                ++res;
            }
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

