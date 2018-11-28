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
        string s1, s2;
        cin >> s1 >> s2;

        vector<char*> c;

        for (i64 i = 0; i < s1.size(); i++) {
            if (s1[i] == '?') {
                c.push_back((char*)s1.c_str() + i);
            }
        }

        for (i64 i = 0; i < s2.size(); i++) {
            if (s2[i] == '?') {
                c.push_back((char*)s2.c_str() + i);
            }
        }

        i64 m = pow(10, c.size());
        i64 M = 1000000;
        i64 C = 1000000;
        string r1, r2;
        for (i64 j = 0; j < m; j++) {
            stringstream ss;
            ss << setw(c.size()) << setfill('0') << j;
            string s = ss.str();
            for (i64 i = 0; i < c.size(); i++) {
                *c[i] = s[i];
            }
            i64 t1, t2;
            stringstream(s1) >> t1;
            stringstream(s2) >> t2;
            if (abs(t1 - t2) < M) {
                M = abs(t1 - t2);
                C = t1;
                r1 = s1;
                r2 = s2;
            }
            else if (abs(t1 - t2) == M) {
                if (t1 < C) {
                    M = abs(t1 - t2);
                    C = t1;
                    r1 = s1;
                    r2 = s2;
                }
            }
        }

        cout << "Case #" << tt << ": ";
        cout << r1 << " " << r2;

        cout << endl;

    }

    return 0;
}