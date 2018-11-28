#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

const int N_MAX = 10005;

int N, X, sizes[N_MAX];

bool works(int twos) {
    for (int i = 0; i < twos; i++) {
        if (sizes[i] + sizes[2 * twos - 1 - i] > X) {
            return false;
        }
    }

    return true;
}

void solve_case(int test_case) {
    scanf("%d %d", &N, &X);

    for (int i = 0; i < N; i++) {
        scanf("%d", &sizes[i]);
    }

    sort(sizes, sizes + N);
    int lo = 0, hi = N / 2;

    while (lo < hi) {
        int mid = (lo + hi + 1) >> 1;

        if (works(mid)) {
            lo = mid;
        } else {
            hi = mid - 1;
        }
    }

    int twos = lo;
    printf("Case #%d: %d\n", test_case, N - twos);
}

int main() {
    int T; scanf("%d", &T);

    for (int tc = 1; tc <= T; tc++) {
        solve_case(tc);
        fflush(stdout);
    }

    return 0;
}
