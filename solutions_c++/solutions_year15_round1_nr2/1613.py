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

int gcd (int a, int b) {
	return b ? gcd (b, a % b) : a;
}

int lcm (int a, int b) {
	return a / gcd (a, b) * b;
}

int main(){
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w", stdout );

    int tc; cin >> tc;
    for ( int _ = 0; _ < tc; _++ ) {
        int n, b;
        int m[1000];
        
        cin >> b >> n;
        for (int i = 0; i < b; i++) {
            cin >> m[i];
        }
        
        int res;
        if (n > b) {
            long long l = 1, r = 2000000000000000000LL;
            long long cnt;
            while(l < r) {
                long long mid = 1LL * l + (r-l)/2;
                
                cnt = 0;
                for (int i = 0; i < b; i++) {
                    if (m[i] <= mid) {
                        cnt += 1LL * (mid / m[i]) + 1;
                    }
                }
                if (cnt < n) {
                    l = mid + 1;
                }
                else {
                    r = mid;
                }
            }
            
            cnt = 0;
            for (int i = 0; i < b; i++) {
                if (m[i] <= l) {
                    cnt += 1LL * (l / m[i]) + 1;
                }
            }

            vector<int> x;
            for (int i = 0; i < b; i++) {
                if (l % m[i] == 0) {
                    x.push_back(i);
                }
            }
            sort(x.begin(), x.end());
            res = x[x.size() - 1 - (cnt-n)] + 1;
        }
        else {
            res = n;
        }
        
        printf("Case #%d: %d\n", _+1, res);
    }
    
    return 0;
}