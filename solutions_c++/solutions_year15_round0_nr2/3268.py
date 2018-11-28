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

int getMax(int arr[], int n) {
    int res = arr[0];
    for ( int i = 1; i < n; i++ ) {
        res = max(res, arr[i]);
    }
    
    return res;
}

int cnt(int val, int bound) {
    return (val / bound) - (val % bound == 0);
}

int main(){
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w", stdout );

    int tc; cin >> tc;
    for ( int _ = 0; _ < tc; _++ ) {
        int arr[5010];
        int d; cin >> d;
        
        for ( int i = 0; i < d; i++ ) {
            cin >> arr[i];
        }
        sort(arr, arr+d);
        
        int res = getMax(arr, d);

        for (int spec = 1; spec < 1000; spec++) {
            int l = 1, r = 1000;
            while (l < r) {
                int mid = l + (r-l)/2;
                int rem = spec;
                
                for (int i = 0; i < d; i++) {
                    if (arr[i] > mid) {
                        rem -= cnt(arr[i], mid);
                        if (rem < 0) {
                            l = mid + 1; break;
                        }
                    }
                }
                if (rem >= 0) {
                    r = mid;
                }
            }
            res = min(res, spec + l);
        }
        
        printf( "Case #%d: %d\n", _+1, res );
    }
    
    return 0;
}