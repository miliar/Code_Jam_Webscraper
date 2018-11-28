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
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <climits>
//#define NDEBUG
#include <cassert>
using namespace std;
#define memsetz(NAME) memset(NAME, 0, sizeof(NAME))
typedef long long i64;
i64 r, t;
i64 cal(i64 val) {
    return 2 * val * val + val * (2 * r - 1);
}
int main()
{
    int T;
    scanf("%d", &T);
    int casenum = 1;
    while (T--) {
        printf("Case #%d: ", casenum++);
        scanf("%lld%lld", &r, &t);
        i64 lo = 1;
        i64 hi = sqrt(double(t / 2)) + 1;
        hi = min(hi, t / (2 * r - 1) + 1);
        hi = max(lo, hi);
        i64 maxv = 1;
        while (1) {
            i64 mid = (hi + lo) / 2;
            i64 temp = cal(mid);
            //cout << mid << ' ' << temp << endl;
            if (hi <= lo) {
                for (i64 ss = hi - 1; ss <= hi + 1; ss++) {
             //   cout << ss << ' ' << cal(ss) << endl;
                    if (cal(ss) <= t) {
                        maxv = ss;
                    }
                }
                break;
            }
            if (temp == t) {
                maxv = mid;
                break;
            } else if (temp < t) {
                lo = mid + 1;
            } else hi = mid - 1;
        }
        printf("%lld\n", maxv);
    }
	return 0;
}
