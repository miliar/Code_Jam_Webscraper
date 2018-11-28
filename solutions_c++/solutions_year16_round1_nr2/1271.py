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


i64 T;

i64 n;
i64 a[103][52];

i64 c[2504];

int main() {
    ios_base::sync_with_stdio(false);


    cin >> T;

    for (i64 tt = 1; tt <= T; tt++) {
        cin >> n;

        for (i64 i = 0; i < 2 * n - 1; i++) {
            for (i64 j = 0; j < n; j++) {
                cin >> a[i][j];
            }
        }


        cout << "Case #" << tt << ": ";


        for (i64 i = 0; i <= 2500; i++) {
            c[i] = 0;
        }

        vector<i64> r;
        for (i64 i = 0; i < 2 * n - 1; i++) {
            for (i64 j = 0; j < n; j++) {
                c[a[i][j]]++;
            }
        }

        for (i64 i = 0; i <= 2500; i++) {
            if (c[i] % 2) {
                r.push_back(i);
            }
        }


        for (i64 i = 0; i < r.size(); i++) {
            cout << r[i] << " ";
        }
        cout << endl;
    }

    return 0;
}