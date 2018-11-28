#include <cstdio>
#include <cstring>
#include <cassert>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <bitset>
#include <cmath>

using namespace std;

#define DBG(z) cerr << #z << ": " << (z) << endl
#define NEWL cerr << endl
#define passert(x, m) {if (!(x)) {cerr << m << "  ::  ";} assert(x);}
#define err(s) cerr << "[92m" << s << "[0m" << endl
#define LINE cerr << "DEBUG LINE: " << __LINE__ << endl

#define IT(v) __typeof((v).begin())
#define mem(f, a) memset(f, a, sizeof(f))
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define for_each(it, v) for (__typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define next_int() ({int __t; scanf("%d", &__t); __t;})


bool pyramid(const vector <int> &a) {
    if (a.size() == 1) return true;
    int i;
    for (i = 0; i + 1 < a.size(); ++i)
        if (a[i + 1] < a[i])
            break;
    for (; i + 1 < a.size(); ++i)
        if (a[i + 1] > a[i])
            return false;
    return true;
}

int diff(vector <int> a, const vector <int> &b) {
    int cnt = 0;
    for (int i = 0; i < b.size(); ++i) {
        int j;
        for (j = i; j < a.size(); ++j) {
            if (a[j] == b[i]) break;
        }
        while (j > i) swap(a[j], a[j - 1]), ++cnt, --j;
    }
    return cnt;
}

int main() {
    int T = next_int();
    for (int kase = 1; kase <= T; ++kase) {
        int N = next_int();
        vector <int> a(N), t(N), b(N);
        for (int i = 0; i < N; ++i) 
            a[i] = next_int(), t[i] = i;


        int res = N * (N + 1) + 100;

        do {
            for (int i = 0; i < N; ++i)
                b[i] = a[t[i]];

            if (pyramid(b))
                res = min(res, diff(a, b));
        } while (next_permutation(all(t)));

        printf("Case #%d: %d\n", kase, res);
    }
}

