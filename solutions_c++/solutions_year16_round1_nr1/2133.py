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

    int T, t;
    char s[1005];
    char ans[3000];

    scanf("%d", &T);

    for(t = 1; t<= T; ++t) {
        scanf("%s", s);

        int start = 1500, end = 1500;

        int i = 0;

        while(s[i]) {
            if(i == 0) {
                ans[start] = s[i];
            } else if(s[i] >= ans[start]) {
                ans[start-1] = s[i];
                start--;
            } else {
                ans[end+1] = s[i];
                end++;
            }
            i++;
        }

        end++;
        ans[end] = 0;

        printf("Case #%d: %s", t, ans+start);
        if(t != T) printf("\n");
    }

    return 0;
}
