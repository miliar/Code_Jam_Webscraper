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

    int t, T, i, ans;
    char in[110];

    scanf("%d",&T);

    for(t = 1; t <= T; ++t) {
        scanf("%s", in);
        ans = i = 0;

        while(in[i]) {
            int minusPresent = 0;
            while(in[i] && in[i] == '-') {
                ++i;
                minusPresent = 1;
            }
            if(minusPresent == 1) {
                ++ans;
            }

            int plusPresent = 0;
            while(in[i] && in[i] == '+') {
                ++i;
                plusPresent = 1;
            }
            if(plusPresent && in[i]) {
                ++ans;
            }
        }

        printf("Case #%d: %d", t, ans);
        if(t != T) {
            printf("\n");
        }
    }

    return 0;
}
