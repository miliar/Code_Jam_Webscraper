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

int ans[1111111];
int w[11];

int f(int n) {
    int c = 10;
    memset(w, 0, sizeof w);
    for(int i = 1; c > 0; ++i) {
        int tmp = n * i;
        while (tmp) {
            if (!w[tmp%10]) {
                w[tmp%10] = 1;
                c--;
            }
            tmp /= 10;
        }
        if (c == 0)
            return n * i;
    }
    return -1;
}

int main() {
    ios::sync_with_stdio(0);
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    
    for(int i = 1; i <= 1e6; ++i)
        ans[i] = f(i);
    
    int t, n;
    cin >> t;
    for(int T = 1; T <= t; ++T) {
        cin >> n;
        cout << "Case #" << T << ": ";
        if (n == 0)
            cout << "INSOMNIA\n";
        else
            cout << ans[n] << "\n";
    }
    return 0;
}