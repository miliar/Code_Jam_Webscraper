#include <iostream>
#include <iomanip>
#include <sstream>
#include <stdint.h>

#include <math.h>

#include <vector>
#include <list>

#include <set>
#include <map>

#include <string>
#include <vector>

#define sqr(x) x * x

#include <algorithm>
#include <functional>

typedef uint32_t u32;
typedef int32_t i32;

typedef uint64_t u64;
typedef int64_t i64;


using namespace std;

struct less_key
{
    bool operator() (const pair<u64, char>& p1, const pair<u64, char>& p2)
    {
        return p1.second > p2.second || (p1.second == p2.second && p1.first > p2.first);
    }
};


i64 tt;


i32 p[10];
i32 a[10];

int main() {
    cin >> tt;


    for (i64 t = 1; t <= tt; t++) {
        i64 r, c, w;
        cin >> r >> c >> w;

        i64 res;

        if (r == 1) {
            if (2 * w > c) {
                res = w + 1;
            }
            else {
                res = c / w + w;
            }
            if (c % w == 0) {
                res--;
            }
        }
        else {
            if (2 * w > c) {
                res = r - 1 + w + 1;
            }
            else {
                res = r * (c / w) + w;
            }
            if (c % w == 0) {
                res--;
            }
        }

        cout << "Case #" << t << ": " << res << endl;
    }

    return 0;
}