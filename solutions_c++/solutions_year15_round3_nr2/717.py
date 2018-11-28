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

double pro;
i32 M;
map<char, i32> p;

void solve(i32 i, string& S, string& K, string& L) {
    if (i >= S.size()) {
        i32 res = 0;
        for (i32 j = 0; j <= S.size() - L.size(); j++) {
            if (S.substr(j, L.size()) == L) {
                res++;
            }
        }
        if (res > 0) {
            M = max(res, M);
            i64 t = 1;
            i64 b = 1;
            for (i32 j = 0; j < S.size(); j++) {
                t *= p[S[j]];
                b *= K.size();
            }
            pro += static_cast<double>(t) * res / b;
        }
    }
    else {
        for (auto it = p.begin(); it != p.end(); it++) {
            S[i] = it->first;
            solve(i + 1, S, K, L);
        }
    }
}

int main() {
    cin >> tt;


    for (i64 t = 1; t <= tt; t++) {
        i64 k, l, s;
        cin >> k >> l >> s;

        string K, L;
        cin >> K >> L;

        //i32 over;
        //for (over = L.size() - 1; over > 0; over--) {
        //    if (L.substr(0, over) == L.substr(L.size() - over)) {
        //        break;
        //    }
        //}


        //i32 M;
        //if (over > 0) {
        //    M = 1 + (s - l) / (l - over);
        //}
        //else {
        //    M = s / l;
        //}

        pro = 0;
        M = 0;
        p.clear();

        for (i32 i = 0; i < K.size(); i++) {
            p[K[i]]++;
        }


        string S;
        S.resize(s);
        solve(0, S, K, L);

        cout << "Case #" << t << ": " << setprecision(6) << fixed << M - pro << endl;
    }

    return 0;
}