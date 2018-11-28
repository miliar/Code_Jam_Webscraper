//#include "testlib.h"
//#include <spoj.h>

#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>
#include <assert.h>
#include <time.h>
#include <memory.h>
#include <set>
#include <numeric>
#include <map>
#include <queue>
#include <stack>
#include <bitset>
#include <unordered_map>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        int k, ans = 0;
        string s;
        cin >> s >> k;
        for(int i = 0; i + k - 1 < s.size(); ++i)
        if (s[i] == '-') {
            ans++;
            for(int j = 0; j < k; ++j) {
                if (s[i+j] == '-')
                    s[i+j] = '+';
                else
                    s[i+j] = '-';
            }
        }
        sort(s.begin(), s.end());
        if (s[0] != s[s.size()-1]) {
            ans = -1;
        }
        
        cout << "Case #" << test << ": ";
        cout << (ans == -1 ? "IMPOSSIBLE" : to_string(ans)) << "\n";
    }
    return 0;
}

