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
i64 N, J;

u64 a[11];
u64 r[11];

const string rs = "3 2 3 2 7 2 3 2 3";

//u64 e[11] = {0, 0, 3, 2, 3, 2, 7, 2, 3, 2, 3};
//
//i64 mpow(i64 n, i64 b) {
//    i64 r = 1;
//    for (i64 i = 1; i <= b; i++) {
//        r *= n;
//    }
//    return r;
//}
//
//i64 check(i64 p) {
//    for (i64 i = 2; i <= trunc(sqrt(p)) + 1; i++) {
//        if (!(p % i)) {
//            return i;
//        }
//    }
//    return 0;
//}

bool check() {
    for (i64 i = 2; i <= 10; i++) {
        switch (i)
        {
        case 3:
        case 5:
        case 7:
        case 9:
            if (a[i] % 2) {
                return false;
            }
            r[i] = 2;
            break;
        case 2:
        case 4:
        case 8:
        case 10:
            if (a[i] % 3) {
                return false;
            }
            r[i] = 3;
            break;
        case 6:
            if (a[i] % 7) {
                return false;
            }
            r[i] = 7;
            break;
        }
        //if (!(r[i] = check(a[i]))) {
        //    return false;
        //}
    }
    return true;
}

int main() {
    ios_base::sync_with_stdio(false);

    cin >> t;

    for (i64 tt = 1; tt <= t; tt++) {
        cin >> N >> J;

        //cout << "Case #" << tt << ": ";
        cout << "Case #" << tt << ":" << endl;

        i64 c = 0;

        for (u64 j = (1ull << (N - 1)) + 1; j < (1ull << N); j += 2) {
            std::bitset<16> bs(j);
            for (i64 i = 2; i <= 10; i++) {
                a[i] = strtoll(bs.to_string().c_str(), 0, i);
            }
            if (check()) {
                cout << a[10] << " " << rs << endl;
                c++;
                if (c == J) {
                    break;
                }
                //for (i64 i = 2; i <= 10; i++) {
                //    if (i != 10) {

                //    }
                //    cout << r[i] << " ";
                //}
                //cout << endl;
            }
        }

    }


    return 0;
}