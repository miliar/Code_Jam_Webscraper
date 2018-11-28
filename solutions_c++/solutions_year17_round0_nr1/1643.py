#include <stdio.h>
#include <stdlib.h>

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

typedef uint8_t u8;
typedef int8_t i8;


using namespace std;

struct less_key
{
    bool operator() (pair<i64, i64> p1, pair<i64, i64> p2)
    {
        return (p1.first > p2.first) || ((p1.first == p2.first) && (p1.second < p2.second));
    }
};

struct pair_hash
{
    std::size_t operator()(const pair<i64, i64>& k) const
    {
        return static_cast<size_t>(k.first ^ k.second);
    }
};

const i64 mod = 100000000007ll;
const i64 inf = 10000000000000007ll;

i64 n;

i64 T;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> T;

    for (i64 tt = 1; tt <= T; tt++) {
        vector<i64> v;
        string s;
        i64 k;
        cin >> s >> k;
        v.resize(s.size() + 1);

        i64 q = 0;
        i64 r = 0;
        for (i64 i = 0; i < s.size() - (k - 1); ++i) {
            if (v[i]) {
                --q;
            }
            if (((s[i] == '+' ? 0 : 1) + q) % 2 == 0) {
                continue;
            }
            v[i + k] = 1;
            ++r;
            ++q;
        }

        i64 f = true;
        for (i64 i = s.size() - (k - 1); i < s.size(); ++i) {
            if (v[i]) {
                --q;
            }
            if (((s[i] == '+' ? 0 : 1) + q) % 2) {
                f = false;
                break;
            }
        }

        cout << "Case #" << tt << ": ";
        if (f) {
            cout << r << endl;
        }
        else {
            cout << "IMPOSSIBLE" << endl;
        }
    }

    return 0;
}