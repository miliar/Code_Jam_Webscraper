/* @coder: Sidharth Gupta */

#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
#include <cassert>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>


#define MOD 109546051211ll
#define MIN(a,b) ((a)>(b)?(b):(a))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define ABS(a) MAX(a,-(a))
#define SET(a,b) memset(a, b, sizeof(a))
#define EVEN(a) ((a&1)==0)
#define SQR(a) ((a)*(a))
#define EPS 0.0001

typedef long long int lli;
typedef unsigned long long int llui;
typedef unsigned int uint;

using namespace std;

int main() {
    int T, i, j, t, N, cnt;
    int mp[11];

    scanf("%d", &T);

    for(t = 1; t <= T; ++t) {
        scanf("%d", &N);
        cnt = 0;
        SET(mp, 0);

        for(i = 1; i <= 100; ++i) {
            int prod = N*i;

            while(prod) {
                int r = prod%10;
                prod /= 10;
                if(mp[r] == 0) {
                    ++cnt;
                    mp[r] = 1;
                }
            }
            if(cnt == 10) {
                printf("Case #%d: %d", t, N*i);
                break;
            }
        }

        if(i == 101) {
            printf("Case #%d: INSOMNIA", t);
        }
        if(t != T) {
            printf("\n");
        }
    }

    return 0;
}
