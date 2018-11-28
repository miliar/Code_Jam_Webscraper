#include <stdio.h>

#include <iostream>
#include <iomanip>
#include <sstream>
#include <stdint.h>
#include <string.h>

#include <unordered_set>

//#define _USE_MATH_DEFINES
//#include <math.h>

#define M_PI 3.14159265358979323846


#include <vector>
#include <list>

#include <set>
#include <map>

#include <unordered_map>

#include <queue>

#include <string>

#include <vector>

#define sqr(x) (x) * (x)

#define eps 1e-7

#include <algorithm>
#include <functional>

#include <bitset>

typedef uint32_t u32;
typedef int32_t i32;

typedef uint64_t u64;
typedef int64_t i64;

typedef uint16_t u16;
typedef int16_t i16;

using namespace std;

struct less_key
{
    bool operator() (const pair<i64, i64>& p1, const pair<i64, i64>& p2)
    {
        return p1.first < p2.first || (p1.first == p2.first && p1.second > p2.second);
    }
};

struct pair_hash
{
    std::size_t operator()(const pair<i64, i64>& k) const
    {
        return static_cast<size_t>(k.first ^ k.second);
    }
};

i64 t;

i64 k, c, s;

i64 get(i64 i, i64 j) {
    return (i - 1) * k + j;
}

int main() {
    ios_base::sync_with_stdio(false);

    cin >> t;

    for (i64 tt = 1; tt <= t; tt++) {
        cin >> k >> c >> s;

        cout << "Case #" << tt << ": ";

        if (s * c < k) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        for (i64 j = 1; j <= k; j++) {
            i64 q = j;
            for (i64 i = 1; i < c; i++) {
                if (j < k) {
                    j++;
                }
                q = get(q, j);
            }
            cout << q << " ";
        }
        cout << endl;
    }

    return 0;
}