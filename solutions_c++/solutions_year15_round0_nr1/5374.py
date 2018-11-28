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
        
        int n, ans = 0, cc = 0;
        string s;
        cin >> n >> s;
        for(int i = 0; i < n+1; ++i) {
            while (cc < i && s[i] > '0') {cc++, ans++;}
            cc += (s[i]-'0');
        }
        cout << ans << "\n";
    }
    return 0;
}
