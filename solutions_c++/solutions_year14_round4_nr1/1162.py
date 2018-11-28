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

const int INF = 10000000;

int N, a[100001], X, taken[100001];

int main() {
    int T = next_int();
    for (int kase = 1; kase <= T; ++kase) {
        mem(taken, 0);
        N = next_int(), X = next_int();
        for (int i = 0; i < N; ++i)
            a[i] = next_int();
        sort(a, a + N);
        int cnt = 0;
        for (int i = N - 1; i >= 0; --i) {
            if (taken[i]) continue;
            for (int j = i - 1; j >= 0; --j) {
                if (!taken[j] && a[i] + a[j] <= X) {
                    taken[j] = taken[i] = true;
                    ++cnt;
                    break;
                }
            }
            if (!taken[i]) taken[i] = true, ++cnt;
        }
        printf("Case #%d: %d\n", kase, cnt);
    }
}

