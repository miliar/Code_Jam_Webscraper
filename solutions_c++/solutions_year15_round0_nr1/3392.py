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
        int s; scanf("%d ", &s);
        
        char arr[1010];
        for ( int i = 0; i <= s; i++ ) {
            cin >> arr[i];
            arr[i] -= '0';
        }
        
        int val = arr[0];
        int res = 0;
        for ( int i = 1; i <= s; i++ ) {
            if (arr[i] == 0) {
                continue;
            }
            
            if (i <= val) {
                val += arr[i];
            }
            else {
                res += i - val;
                val += arr[i] + i - val;
            }
        }
        
        printf( "Case #%d: %d\n", _+1, res );
    }
    
    return 0;
}