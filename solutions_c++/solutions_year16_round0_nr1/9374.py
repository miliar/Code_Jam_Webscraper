#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <algorithm>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <sstream>
#include <complex>
#include <cassert>

using namespace std;
typedef long long ll;
typedef vector<int> VI;
typedef pair<int, int> PII;

#define REP(i,s,t) for(int i=(s);i<(t);i++)
#define FILL(x,v) memset(x,v,sizeof(x));


int main() {

    int T, cas = 1;
    scanf("%d", &T);
    while (T--) {
        ll n;
        scanf("%lld", &n);
        int mask = 0;
        int cur = 0;
        ll k = n;
        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", cas++);
            continue;
        }
        do {
            k = n * ++cur;
            while (k > 0) {
                int digit = k % 10;
                k /= 10;
                mask |= (1 << digit);
                if (mask == (1 << 10) - 1) break;
            }
        } while (mask != (1 << 10) - 1);
        printf("Case #%d: %lld\n", cas++, n*cur);
    }

    return 0;
}
