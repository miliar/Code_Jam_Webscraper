#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

vector <long long> fsq;

long long make_palindrom(long long base, bool repeat_last) {
    long long t = base;

    if (!repeat_last) {
        base /= 10;
    }

    for ( ; base; base /= 10) {
        t *= 10;
        t += (base % 10);
    }

    return t;
}

bool check_palindrom(long long t) {
    long long reversed = 0;

    for (long long i = t; i; i /= 10) {
        reversed *= 10;
        reversed += (i % 10);
    }

    return t == reversed;
}

void find_all_fair_square() {
    long long t;
    for (long long i = 1; i < 10000LL; ++i) {
        t = make_palindrom(i, true);
        if (check_palindrom(t*t)) {
            //printf("%lld %lld\n", i, t*t);
            fsq.push_back(t*t);
        }
        t = make_palindrom(i, false);
        if (check_palindrom(t*t)) {
            //printf("%lld %lld\n", i, t*t);
            fsq.push_back(t*t);
        }
    }
}

int main() {
    int T;
    scanf("%d", &T); 

    find_all_fair_square();

    sort(fsq.begin(), fsq.end());

    for (int tt = 1; tt <= T; ++tt) {
        long long A, B;
        scanf("%lld%lld", &A, &B);
        int t = lower_bound(fsq.begin(), fsq.end(), B+1) - lower_bound(fsq.begin(), fsq.end(), A);
        printf("Case #%d: %d\n", tt, t);
    }
    return 0;
}
