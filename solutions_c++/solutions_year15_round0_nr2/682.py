#include <iostream>
#include <iomanip>
#include <sstream>
#include <stdint.h>
#include <string.h>

#include <unordered_set>
#include <unordered_map>

#include <vector>
#include <list>

#include <set>
#include <map>

#include <string>
#include <vector>
#include <queue>

#include <algorithm>
#include <functional>

typedef uint8_t u8;
typedef int8_t i8;


typedef uint32_t u32;
typedef int32_t i32;

typedef uint64_t u64;
typedef int64_t i64;

#define sqr(x) x*x

#define INF 20000000000000000
#define MOD 1000000007

using namespace std;

struct less_key
{
    bool operator() (const pair<u32, u32>& p1, const pair<u32, u32>& p2)
    {
        return p1.first < p2.first || (p1.first == p2.first && p1.second < p2.second);
    }
};

u32 t;
u32 d;
u32 p[1001];

int main() {
    cin >> t;

    for (u32 tt = 0; tt < t; tt++) {
        u32 m = 0;

        cin >> d;
        for (u32 i = 0; i < d; i++) {
            cin >> p[i];
            m = max(m, p[i]);
        }

        u32 r = m;
        sort(p, p + d);

        for (u32 i = 1; i < m; i++) {
            u32 c = i;
            for (u32 j = upper_bound(p, p + d, i) - p; j < d; j++) {
                c += p[j] / i + (p[j] % i ? 1 : 0) - 1;
            }
            r = min(c, r);
        }

        cout << "Case #" << tt + 1 << ": " << r << endl;
    }

    return 0;
}