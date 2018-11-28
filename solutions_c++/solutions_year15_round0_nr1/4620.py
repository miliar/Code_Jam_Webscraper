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

const int MAXN = 1010;
const int MOD = 1000000007;

char shy[MAXN];

int main ()
{
    int TT;
    scanf("%d", &TT);
    for (int tt = 1; tt <= TT; tt++) {
        int N;
        scanf("%d", &N);
        scanf("%s", shy);
        for (int i = 0; i < N + 1; i++) {
            shy[i] -= '0';
        }
        int friends = 0;
        int up = shy[0];
        for (int i = 1; i <= N + 1; i++) {
            if (!shy[i]) continue;
            if (up < i) {
                friends += i - up;
                up = i;
            }
            up += shy[i];
        }
        printf("Case #%d: %d\n", tt, friends);
    }
    return 0;
}
