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
    bool operator() (pair<i64, i64> p1, pair<i64, i64> p2)
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

char a[8];
i64 q[8];

i64 n;
i64 r, p, s;


string split1(set<pair<i64, char> >& q);
string split2(set<pair<i64, char> >& q);

string split1(set<pair<i64, char> >& q) {
    auto i1 = q.begin();
    auto i2 = i1; i2++;
    auto i3 = i2; i3++;

    if (!i1->first) {
        stringstream ss;
        ss << i2->second << i3->second;
        return ss.str();
    }

    set<pair<i64, char> > q1;
    q1.insert(make_pair(i1->first / 2    , i1->second));
    q1.insert(make_pair(i2->first / 2 + 1, i2->second));
    q1.insert(make_pair(i3->first / 2    , i3->second));

    set<pair<i64, char> > q2;
    q2.insert(make_pair(i1->first / 2    , i1->second));
    q2.insert(make_pair(i2->first / 2    , i2->second));
    q2.insert(make_pair(i3->first / 2 + 1, i3->second));

    return split2(q1) + split2(q2);
}

string split2(set<pair<i64, char> >& q) {
    auto i1 = q.begin();
    auto i2 = i1; i2++;
    auto i3 = i2; i3++;

    set<pair<i64, char> > q1;
    q1.insert(make_pair(i1->first / 2 + 1, i1->second));
    q1.insert(make_pair(i2->first / 2    , i2->second));
    q1.insert(make_pair(i3->first / 2    , i3->second));

    set<pair<i64, char> > q2;
    q2.insert(make_pair(i1->first / 2    , i1->second));
    q2.insert(make_pair(i2->first / 2 + 1, i2->second));
    q2.insert(make_pair(i3->first / 2    , i3->second));

    return split1(q1) + split1(q2);
}

//string split(set<pair<i64, char> > q, i64 n) {
//    if (n % 2) {
//        return split1(q, n);
//    }
//    else {
//        return split2(q, n);
//    }
//}

int main() {
    ios_base::sync_with_stdio(false);

    cin >> T;

    for (i64 tt = 1; tt <= T; tt++) {

        cin >> n >> r >> p >> s;

        set<pair<i64, char> > q;
        q.insert(make_pair(r, 'R'));
        q.insert(make_pair(p, 'P'));
        q.insert(make_pair(s, 'S'));


        auto i1 = q.begin();
        auto i2 = i1; i2++;
        auto i3 = i2; i3++;

        string R;

        if (n % 2) {
            if (!(i1->first + 1 == i2->first && i2->first == i3->first)) {
                cout << "Case #" << tt << ": ";
                cout << "IMPOSSIBLE";
                cout << endl;
                continue;
            }
            R = split1(q);
        }
        else {
            if (!(i1->first == i2->first && i2->first + 1 == i3->first)) {
                cout << "Case #" << tt << ": ";
                cout << "IMPOSSIBLE";
                cout << endl;
                continue;
            }
            R = split2(q);
        }

        cout << "Case #" << tt << ": ";
        cout << R;
        cout << endl;

    }

    return 0;
}