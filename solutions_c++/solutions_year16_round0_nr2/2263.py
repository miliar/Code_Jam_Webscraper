#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <bitset>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <memory.h>
#include <cmath>

using namespace std;

#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define FOR0(i,n) for( i = 0 ; i < n ; ++i )
#define FOR1(i,n) for( i = 1 ; i <= n ; ++i )
#define sys_p system( "pause" )
#define pb push_back
#define mp make_pair
#define FI first
#define SE second
#define sz(a) (int)a.size()

typedef long long LL;

int lpos, diff,n;
string s;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int T, T_, N, i;
    scanf("%d", &T);
    FOR1(T_, T) {
        printf("Case #%d: ", T_);
        cin >> s;
        n = (int) s.length();
        lpos = n;
        for (i = n-1; i >= 0; --i)
            if (s[i] == '-') {
                lpos = i;
                break;
            }
        diff = 0;
        if (lpos < n) {
            FOR1(i, lpos)
                if (s[i] != s[i-1])
                    diff += 1;
            diff += 1;
        }
        printf("%d\n", diff);
    }
    return 0;
}
