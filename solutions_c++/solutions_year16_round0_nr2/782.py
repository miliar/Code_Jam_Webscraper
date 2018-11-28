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

string n;


string s;

int main() {
    ios_base::sync_with_stdio(false);

    cin >> t;
    getline(cin, s);

    for (i64 i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";

        getline(cin, s);

        s = s[0] + s;
        i64 q = 0;

        for (i64 i = 1; i < s.size(); i++) {
            if (s[i] != s[i - 1]) {
                q++;
            }
        }
        cout << q + (s[s.size() - 1] == '-' ? 1 : 0) << endl;
    }


    return 0;
}