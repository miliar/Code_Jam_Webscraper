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

#include <algorithm>
#include <functional>

#include <bitset>

#include <functional>

typedef uint32_t u32;
typedef int32_t i32;

typedef uint64_t u64;
typedef int64_t i64;

typedef uint16_t u16;
typedef int16_t i16;

using namespace std;

struct less_key
{
    bool operator() (i64 p1, i64 p2)
    {
        return p1 > p2;
    }
};

struct pair_hash
{
    std::size_t operator()(const pair<i64, i64>& k) const
    {
        return static_cast<size_t>(k.first ^ k.second);
    }
};

i64 T;


u64 pow(i64 n) {
    i64 r = 1;
    for (i64 i = 0; i < n; i++) {
        r <<= 1;
    }
    return r;
}

int main() {
    ios_base::sync_with_stdio(false);

    cin >> T;


    for (i64 tt = 1; tt <= T; tt++) {
        i64 b;
        u64 m;

        cin >> b >> m;

        if (m > pow(b - 2)) {
            cout << "Case #" << tt << ": ";
            cout << "IMPOSSIBLE";
            cout << endl;
            continue;
        }

        stringstream ss;
        ss << 0;
        u64 t = pow(b - 3);
        for (i64 i = 2; i <= b - 1; i++) {
            if (m >= t) {
                ss << 1;
                m -= t;
            }
            else {
                ss << 0;
            }
            t >>= 1;
        }

        if (m) {
            ss << 1;
        }
        else {
            ss << 0;
        }

        cout << "Case #" << tt << ": ";
        cout << "POSSIBLE" << endl;
        cout << ss.str() << endl;

        for (i64 i = 2; i <= b - 1; i++) {
            stringstream ss;
            for (i64 j = 1; j <= b; j++) {
                if (j <= i) {
                    ss << 0;
                }
                else {
                    ss << 1;
                }
            }
            cout << ss.str() << endl;
        }
        stringstream ss1;
        for (i64 j = 1; j <= b; j++) {
            ss1 << 0;
        }
        cout << ss1.str() << endl;
    }



    return 0;
}