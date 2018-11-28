#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <ctime>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

template<class T> inline T cabs(const T &x) { return x > 0 ? x : (-x); }
template<class T> inline T gcd(const T &x, const T &y) { return (y == 0) ? x : gcd(y, x % y); }
template<class T> inline T sgn(const T &x) { return (x > 0) - (x < 0); }

#define dbg(x) cout << #x << " = " << (x) << endl
#define dbg2(x,y) cout << #x << " = " << (x) << ", " << #y << " = " << (y) << endl
#define dbg3(x,y,z) cout << #x << " = " << (x) << ", " << #y << " = " << (y) << ", " << #z << " = " << (z) << endl
#define dbg4(x,y,z,w) cout << #x << " = " << (x) << ", " << #y << " = " << (y) << ", " << #z << " = " << (z) << ", " << #w << " = " << w << endl

#define out(x) cout << (x) << endl
#define out2(x,y) cout << (x) << " " << (y) << endl
#define out3(x,y,z) cout << (x) << " " << (y) << " " << (z) << endl
#define out4(x,y,z,w) cout << (x) << " " << (y) << " " << (z) << " " << (w) << endl

const int maxN = 128;

char str[maxN];

int run() {
    int len = strlen(str);
    int res = 0;
    for(int i = len - 1; i >= 0; i --) {
        if( str[i] == '+' )
            continue;
        else {
            if( str[0] == '-' ) {
                res ++;
                for(int j = 0, k = i; j < k; j ++, k --)
                    swap(str[j], str[k]);
                for(int j = 0; j <= i; j ++) {
                    if( str[j] == '-' )
                        str[j] = '+';
                    else
                        str[j] = '-';
                }
            } else {
                res ++;
                for(int j = 0; j <= i; j ++) {
                    if( str[j] == '+' )
                        str[j] = '-';
                    else
                        break;
                }
                res ++;
                for(int j = 0, k = i; j < k; j ++, k --)
                    swap(str[j], str[k]);
                for(int j = 0; j <= i; j ++) {
                    if( str[j] == '-' )
                        str[j] = '+';
                    else
                        str[j] = '-';
                }
            }
        }
    }
    return res;
}

int main()
{
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    int nt, idx = 0;
    scanf("%d", &nt);
    for(; nt > 0; nt --) {
        scanf("%s", str);
        printf("Case #%d: %d\n", ++ idx, run());
    }
    return 0;
}
