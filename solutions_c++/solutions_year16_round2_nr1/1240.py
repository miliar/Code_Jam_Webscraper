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

void skip(string t, i64 m, i64 c[256]) {
    for (i64 i = 0; i < t.size(); i++) {
        c[t[i]] -= m;
    }
}

i64 T;

int main() {
    ios_base::sync_with_stdio(false);

    cin >> T;


    for (i64 tt = 1; tt <= T; tt++) {
        string s;
        cin >> s;

        i64 d[10] = { 0 };
        i64 c[256] = { 0 };

        for (i64 i = 0; i < s.size(); i++) {
            c[s[i]]++;
        }

        d[0] = c['Z'];
        skip("ZERO", c['Z'], c);

        d[2] = c['W'];
        skip("TWO", c['W'], c);

        d[4] = c['U'];
        skip("FOUR", c['U'], c);

        d[6] = c['X'];
        skip("SIX", c['X'], c);

        d[8] = c['G'];
        skip("EIGHT", c['G'], c);


        d[1] = c['O'];
        skip("ONE", c['O'], c);

        d[3] = c['R'];
        skip("THREE", c['R'], c);

        d[5] = c['F'];
        skip("FIVE", c['F'], c);

        d[7] = c['V'];
        skip("SEVEN", c['V'], c);

        d[9] = c['I'];
        skip("NINE", c['I'], c);


        cout << "Case #" << tt << ": ";
        for (i64 i = 0; i < 10; i++) {
            for (i64 j = 0; j < d[i]; j++) {
                cout << i;
            }
        }

        cout << endl;

    }

    return 0;
}