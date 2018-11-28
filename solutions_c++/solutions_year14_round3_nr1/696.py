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
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,a)    FOR(i,0,a)
#define MP          make_pair
#define PB          push_back
#define ST          first
#define ND          second

using namespace std;

using VI = vector<int>;
using VVI = vector<VI>;
using PII = pair<int, int>;
using VII = vector<PII>;
using LL = long long int;
using ULL = unsigned long long int;

LL gcd(LL a, LL b) {
    if (a == 0) return b;
    return gcd(b % a, a);
}

void solve() {
    LL a, b;
    char dummy;
    cin >> a >> dummy >> b;

    LL div = gcd(a,b);
    a = a / div;
    b = b / div;

    if ((b & (b - 1)) != 0) {
        cout << "impossible\n";
        return;
    }
    int result = 1;
    LL c = 2;
    while (a * c < b) {
        c *= 2;
        ++result;
    }
    cout << result << "\n";
}



int testCases;

int main() {
    cin >> testCases;
    REP(i, testCases) {
        cout << "Case #" << i+1 << ": ";
        solve();
    }
    return 0;
}

