#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>

using namespace std;

long long calc1(long long k, long long size) {
    if (k == 0) return 0;
    return size / 2 + calc1((k - 1) / 2, size / 2);
}

long long solve1(int n, long long p) {
    long long head = 0;
    long long tail = (1LL << n) - 1;
    while (head <= tail) {
        long long mid = (head + tail) / 2;
        if (calc1(mid, 1LL << n) < p) head = mid + 1; else tail = mid - 1;
    }
    return head - 1;
}

long long calc2(long long k, long long size) {
    if (k == size - 1) return 0;
    return size / 2 + calc2((k + 1) / 2, size / 2);
}

long long solve2(int n, long long p) {
    long long head = 0;
    long long tail = (1LL << n) - 1;
    while (head <= tail) {
        long long mid = (head + tail) / 2;
        if ((1LL << n) - 1 - calc2(mid, (1LL << n)) < p) head = mid + 1; else tail = mid - 1;
    }
    return head - 1;
}

void work() {
    int n;
    long long p;
    scanf("%d%lld", &n, &p);
    printf("%lld %lld\n", solve1(n, p), solve2(n, p));
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int test = 0; test < T; test ++) {
        printf("Case #%d: ", test + 1);
        work();
    }

    return 0;
}