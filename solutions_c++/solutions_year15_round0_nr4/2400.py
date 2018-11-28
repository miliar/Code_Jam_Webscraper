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

int main() {
    ios::sync_with_stdio(0);
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    int t; cin >> t;
    for(int tt = 1; tt <= t; ++tt) {
        cout << "Case #" << tt << ": ";
        
        int x, r, c, ans = 0;
        cin >> x >> r >> c;
        if (c < r) swap(c, r);
     
        switch (x) {
            case 1:
                ans = 1;
                break;
            
            case 2:
                ans = (r * c + 1) % 2;
                break;
            case 3:
                ans = ((c == 3 && (r == 2 || r == 3)) || (c == 4 && r == 3));
                break;
            case 4:
                ans = (c == 4 && r >= 3);
                break;
        }
        
        if (ans)
            cout << "GABRIEL\n";
        else
            cout << "RICHARD\n";
    }
    return 0;
}
