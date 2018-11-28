#include <cassert>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <sstream>
#include <typeinfo>
#include <list>
#include <map>
#include <queue>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <numeric>
#include <utility>
#include <iomanip>
#include <bitset>
#include <fstream>
#include <limits>

using namespace std;

typedef long long int64;

const int MAXLEN = 100;

int64 dp[2][MAXLEN + 1];

void prep() {
    dp[0][0] = dp[1][0] = 0;
    
    dp[0][1] = 0;
    dp[1][1] = 1;

    for (int len = 2; len <= MAXLEN; len++) {
        dp[0][len] = dp[1][len-1] + 1;
        dp[1][len] = dp[0][len-1] + 1;
    }
}

string Simplify(const string& pancakes) {
    string simple;

    char prev = '\0';
    const int N = pancakes.length();

    for (int i = 0; i < N; ++i) {
        if (pancakes[i] != prev) {
            prev = pancakes[i];
            simple += prev;
        }
    }

    return simple;
}

int MinNumFlips(const string& pancakes) {
    string simple = Simplify(pancakes);

    int idx = (simple[0] != '+');
    return dp[idx][simple.length()];
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    prep();

    int T;
    cin >> T;
    cin.ignore();

    for (int test_case = 1; test_case <= T; test_case++) {
        string pancakes;
        cin >> pancakes;

        cout << "Case #" << test_case << ": " << MinNumFlips(pancakes) << "\n";
    }

    return 0;
}
