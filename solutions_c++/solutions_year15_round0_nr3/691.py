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

u32 t;
i64 l;
i64 x;
string r;
string R;

u64 get_loop() {
    i32 s = 1;
    char c = '1';

    u64 m = 0;

    for (;;) {
        m++;
        for (u32 i = 0; i < r.size(); i++) {
            s *= S[c][r[i]];
            c  = M[c][r[i]];
        }
        if (c == '1' && s == 1) {
            break;
        }
    }

    return m;
}

i32 get_i() {
    i32 s = 1;
    char c = '1';

    for (u32 i = 0; i < R.size(); i++) {
        s *= S[c][R[i]];
        c  = M[c][R[i]];

        if (c == 'i' && s == 1) {
            return i;
        }
    }

    return -1;
}

i32 get_k() {
    i32 s = 1;
    char c = '1';

    for (i32 i = R.size() - 1; i >= 0; i--) {
        s *= S[R[i]][c];
        c  = M[R[i]][c];

        if (c == 'k' && s == 1) {
            return i;
        }
    }

    return -1;
}

bool check_j(u32 i, u32 k) {
    i32 s = 1;
    char c = '1';

    for (u32 j = i + 1; j <= k - 1; j++) {
        s *= S[c][R[j]];
        c  = M[c][R[j]];
    }

    return c == 'j' && s == 1;
}


int main() {
    M['1']['1'] = '1';
    M['1']['i'] = 'i';
    M['1']['j'] = 'j';
    M['1']['k'] = 'k';

    M['i']['1'] = 'i';
    M['i']['i'] = '1';
    M['i']['j'] = 'k';
    M['i']['k'] = 'j';

    M['j']['1'] = 'j';
    M['j']['i'] = 'k';
    M['j']['j'] = '1';
    M['j']['k'] = 'i';

    M['k']['1'] = 'k';
    M['k']['i'] = 'j';
    M['k']['j'] = 'i';
    M['k']['k'] = '1';




    S['1']['1'] = 1;
    S['1']['i'] = 1;
    S['1']['j'] = 1;
    S['1']['k'] = 1;

    S['i']['1'] = 1;
    S['i']['i'] = -1;
    S['i']['j'] = 1;
    S['i']['k'] = -1;

    S['j']['1'] = 1;
    S['j']['i'] = -1;
    S['j']['j'] = -1;
    S['j']['k'] = 1;

    S['k']['1'] = 1;
    S['k']['i'] = 1;
    S['k']['j'] = -1;
    S['k']['k'] = -1;



    cin >> t;

    for (u32 tt = 0; tt < t; tt++) {
        cin >> l >> x >> r;

        i64 m = get_loop();
        m = min(m, x);


        R.clear();
        for (u32 i = 0; i < m; i++) {
            R += r;
        }


        i32 ii = get_i();
        if (ii < 0) {
            cout << "Case #" << tt + 1 << ": NO" << endl;
            continue;
        }

        i32 ik = get_k();
        if (ik < 0) {
            cout << "Case #" << tt + 1 << ": NO" << endl;
            continue;
        }

        i32 mi = ii / r.size();
        i32 si = ii % r.size();

        i32 mk = ik / r.size();
        i32 sk = ik % r.size();

        i64 lx = x - mi - (m - 1 - mk);

        if (lx <= 0) {
            cout << "Case #" << tt + 1 << ": NO" << endl;
            continue;
        }

        if (lx == 1) {
            R = r;
        }
        else {
            lx -= 2;
            lx %= m;

            R = r + r;
            for (i64 i = 0; i < lx; i++) {
                R += r;
            }
        }

        if (check_j(si, R.size() - (r.size() - sk))) {
            cout << "Case #" << tt + 1 << ": YES" << endl;
        }
        else {
            cout << "Case #" << tt + 1 << ": NO" << endl;
        }
    }

    return 0;
}