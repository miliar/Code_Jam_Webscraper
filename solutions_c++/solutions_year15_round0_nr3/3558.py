//#include "testlib.h"

#include <iostream>
#include <math.h>
#include <map>
#include <vector>
#include <stdlib.h>
#include <memory.h>
#include <time.h>
#include <string.h>
#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <set>
#include <cassert>
#include <queue>

using namespace std;

int mul[5][5] = { {0,0,0,0,0},
                {0,1,2,3,4},
                {0,2,-1,4,-3},
                {0,3,-4,-1,2},
                {0,4,3,-2,-1}};

int MUL(int a, int b) {
    if (a < 0) a *= -1, b *= -1;
    bool rev = 0;
    if (b < 0) b *= -1, rev = 1;
    int res = mul[a][b];
    if (rev) res *= -1;
    return res;
}

int main() {
    ios::sync_with_stdio(0);
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    int t; cin >> t;
    for(int tt = 1; tt <= t; ++tt) {
        cout << "Case #" << tt << ": ";
        string s;
        int n, x, i = 0, j = 0, k = 0, r = 1;
        cin >> n >> x >> s;
        
        for(int it2 = 0; it2 < x; ++it2)
            for(int it = 0; it < n; ++it) {
                if (s[it] == 'i') r = MUL(r, 2);
                if (s[it] == 'j') r = MUL(r, 3);
                if (s[it] == 'k') r = MUL(r, 4);
                
                if (r == 2)
                    i = 1;
                if (r == 4 && i)
                    j = 1;
                if (r == -1 && j && it2+1 == x && it+1 == n)
                    k = 1;
            }
        
        if (i && j && k)
            cout << "YES\n";
        else
            cout << "NO\n";
    }
    return 0;
}
