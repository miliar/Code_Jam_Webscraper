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

char M[256][256];
i32 S[256][256];

u32 x;
u32 r;
u32 c;
u32 t;


int main() {

    cin >> t;

    for (u32 tt = 0; tt < t; tt++) {
        cin >> x >> r >> c;

        if (r * c % x) {
            cout << "Case #" << tt + 1 << ": " << "RICHARD" << endl;
            continue;
        }

        //if (x >= 7) {
        //    cout << "Case #" << tt + 1 << ": " << "RICHARD" << endl;
        //    continue;
        //}

        if (x == 1 || x == 2) {
            cout << "Case #" << tt + 1 << ": " << "GABRIEL" << endl;
            continue;
        }

        if (x == 3) {
            if (r == 1 || c == 1) {
                cout << "Case #" << tt + 1 << ": " << "RICHARD" << endl;
            }
            else {
                cout << "Case #" << tt + 1 << ": " << "GABRIEL" << endl;
            }
            continue;
        }

        if (x == 4) {
            if (r < 3 || c < 3) {
                cout << "Case #" << tt + 1 << ": " << "RICHARD" << endl;
            }
            else {
                cout << "Case #" << tt + 1 << ": " << "GABRIEL" << endl;
            }
            continue;
        }
    }

    return 0;
}