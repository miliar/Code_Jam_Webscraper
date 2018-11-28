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


int main() {
    ios_base::sync_with_stdio(false);

    cin >> T;


    for (i64 tt = 1; tt <= T; tt++) {
        i64 n;
        i64 a[1004];

        cin >> n;

        for (i64 i = 1; i <= n; i++) {
            cin >> a[i];
        }

        i64 s = 0;
        multimap<i64, char, less_key> m;

        for (i64 i = 1; i <= n; i++) {
            m.insert(make_pair(a[i], (char)('A' + i - 1)));
        }

        vector<string> R;

        while (m.size() != 0) {
            if (m.size() > 2) {
                auto it = m.begin();
                auto p = *it;
                R.push_back(string(1, it->second));
                m.erase(it);
                if (p.first > 1) {
                    m.insert(make_pair(p.first - 1, p.second));
                }
            }
            else {
                auto it1 = m.begin();
                auto it2 = it1;
                it2++;

                R.push_back(string(1, it1->second) + string(1, it2->second));

                auto p1 = *it1;
                auto p2 = *it2;

                m.erase(it1);
                m.erase(it2);

                if (p1.first > 1) {
                    m.insert(make_pair(p1.first - 1, p1.second));
                    m.insert(make_pair(p2.first - 1, p2.second));
                }

            }
        } 




        cout << "Case #" << tt << ": ";

        for (i64 i = 0; i < R.size(); i++) {
            cout << R[i] << " ";
        }

        cout << endl;
    }

    return 0;
}