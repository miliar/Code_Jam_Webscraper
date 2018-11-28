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
    ios::sync_with_stdio(0);
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    
    int t;
    cin >> t;
    for(int T = 1; T <= t; ++T) {
        int k, c, s;
        cin >> k >> c >> s;
        cout << "Case #" << T << ":";
        long long step = 1;
        for(int i = 0; i < c-1; ++i)
            step *= k;
        
        for(int i = 0; i < k; ++i)
            cout << " " << i * step + 1;
        cout << "\n";
    }
    return 0;
}