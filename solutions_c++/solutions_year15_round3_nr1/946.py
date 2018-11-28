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
        int r, c, w;
        cin >> r >> c >> w;
        
        int res = 0;

        if (c == w) {
            res = w;
        }
        else if (c <= w * 2) {
            res = w + 1;
        }
        else {
            res = ((c / w) - 1);
            
            if (c - ((c/w)-1)*w == w) {
                res += w;
            }
            else {
                res += w + 1;
            }
        }
        
        if (r > 1) {
            res += (r - 1) * (c / w);
        }
        
        printf( "Case #%d: %d\n", _+1, res );
    }
    
    return 0;
}