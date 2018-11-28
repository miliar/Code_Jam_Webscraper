#include <assert.h>
#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

typedef unsigned int UINT;
typedef long long unsigned int ULL;
typedef long long int LL;

const int MAXN = 10000000;
const int MOD = 1000000007;

int main ()
{
    int TT;
    scanf("%d", &TT);
    for (int tt = 1; tt <= TT; tt++) {
        int X, R, C;
        scanf("%d %d %d", &X, &R, &C);
        bool win = true;
        if (X == 1) {
            // Gabriel
            win = false;
        } else if (X == 2) {
            if (R*C % 2 == 0) {
                win = false;
            } else {
                win = true;
            }
        } else if (X == 3) {
            if (R*C % 3 != 0 || R*C == 3) {
                win = true;
            } else {
                win = false;
            }
        } else if (X == 4) {
            if (R*C == 12 || R*C == 16) {
                win = false;
            } else {
                win = true;
            }
        }
        printf("Case #%d: %s\n", tt, win ? "RICHARD" : "GABRIEL");
    }
    return 0;
}
