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

u32 a[200];
u32 A[200][200][4];

int main() {
    cin >> t;

    for (u32 tt = 0; tt < t; tt++) {
        u32 smax = 0;
        string s;

        cin >> smax >> s;
        u32 res = 0;
        u32 sum = 0;

        for (u32 i = 0; i <= smax; i++) {
            if (i > sum) {
                res += (i - sum);
                sum = i;
            }
            sum += s[i] - '0';
        }

        cout << "Case #" << tt + 1 << ": " << res << endl;
    }

    return 0;
}