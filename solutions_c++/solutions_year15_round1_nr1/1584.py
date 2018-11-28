#pragma comment (linker, "/STACK:128000000")
#define _CRT_SECURE_NO_DEPRECATE
#define _SECURE_SCL 0
#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

#define MOD 1000000007

using namespace std;

int main(){
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w", stdout );

    int tc; cin >> tc;
    for ( int _ = 0; _ < tc; _++ ) {
        int n; int m[1000];
        cin >> n;
        for (int i = 0; i < n; i++) cin >> m[i];
        
        int diff = 0;
        // strategy 1
        int res1 = 0;
        for ( int i = 1; i < n; i++ ) {
            if (m[i] < m[i-1]) {
                res1 += m[i-1] - m[i];
                diff = max(diff, m[i-1] - m[i]);
            }
        }

        // strategy 2
        int res2 = 0;        
        for (int i = 1; i < n; i++) {
            int step = min(m[i-1], diff);
            res2 += step;
        }
        
        printf("Case #%d: %d %d\n", _+1, res1, res2);
    }
    
    return 0;
}