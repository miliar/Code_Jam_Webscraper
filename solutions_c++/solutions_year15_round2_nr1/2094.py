#include <iostream>
#include <iomanip>
#include <sstream>
#include <stdint.h>

#include <unordered_set>
#include <unordered_map>

#include <math.h>

#include <vector>
#include <list>

#include <set>
#include <map>

#include <string>
#include <vector>

#include <algorithm>

typedef uint32_t u32;
typedef int32_t i32;

typedef uint64_t u64;
typedef int32_t i64;

using namespace std;

struct less_key
{
    bool operator() (const pair<u64, char>& p1, const pair<u64, char>& p2)
    {
        return p1.first < p2.first || (p1.first == p2.first && p1.second < p2.second);
    }
};


i32 n;

i32 tt;

i64 reverse(i64 n) {
    i64 r = 0;
    for (;;) {
        if (!n) {
            break;
        }
        r = r * 10 + n % 10;
        n /= 10;
    }

    return r;
}

i64 m[19];

void solve(vector<i64> f, vector<i64> t, i64& r) {
    i64 c = t.size();

    i64 h = c / 2;

    if (c % 2) {
        r += (t[h] - f[h]) * m[h];
    }

    // high
    for (i32 j = 0; j < h; j++) {
        if (t[j] != f[j]) {
            for (i32 i = 0; i < h; i++) {
                r += (t[i] - f[c - 1 - i]) * m[i];
            }
            r++; // swap
            break;
        }
    }

    // low
    for (i32 i = 0; i < h; i++) {
        r += (t[c - 1 - i] - f[c - 1 - i]) * m[i];
    }
}

void convert(i64 n, vector<i64>& C) {
    for (;;) {
        if (!n) {
            reverse(C.begin(), C.end());
            return;
        }
        C.push_back(n % 10);
        n /= 10;
    }
}

i64 slv(i64 n, bool isr) {
    bool ism = false;
    if (!(n % 10)) {
        n--;
        ism = true;
    }


    if (n < 10) {
        return n + (isr ? 1 : 0) + (ism ? 1 : 0);
    }


    vector<i64> R;

    convert(n, R);


    vector<i64> F;
    vector<i64> T;

    F.push_back(1);
    T.push_back(9);

    i64 r = 1;

    while (1) {
        if (F.size() < R.size()) {
            solve(F, T, r);
        }

        F[F.size() - 1] = 0;
        F[0] = 1;

        T.push_back(9);

        if (F.size() + 1 != R.size()) {
            r += 2;
            F.push_back(1);
        }
        else {
            r++;
            F.push_back(0);
            break;
        }
    }

    for (i32 i = 0; i < R.size(); i++) {
        if (R[i] != F[i]) {
            r++;
            F[F.size() - 1] = 1;
            solve(F, R, r);
            break;
        }
    }

    return r + (isr ? 1 : 0) + (ism ? 1 : 0);
}


int main() {

    i64 I = 1;

    for (i64 i = 0; i <= 18; i++) {
        m[i] = I;
        I *= 10;
    }

    cin >> tt;

    for (i32 t = 1; t <= tt; t++) {
        i64 n;
        cin >> n;

        i64 r = slv(n, false);

        if (n % 10) {
            r = min(r, slv(reverse(n), true));
        }


        cout << "Case #" << t <<": " << r << endl;
    }



    return 0;
}