#include <cstdio>

int N;

bool can_i_win(long long a, long long P) {
    long long slabiji_od_mene = (1LL<<N) - a - 1;

    int t = 0;

    for (int i = (N-1); i >= 0; --i) {
        if (P & (1LL<<i)) {
            t = 1 + ((N-1) - i);
            if (P == (1LL<<(i+1)) - 1) { // if of form 0001111
                --t;
            }
            break;
        }
    }

    if (P == 0) t = N;

    for (int i = 0; i < t; ++i) {
        if (slabiji_od_mene == 0) return false;
        slabiji_od_mene -= 1; // tog ja moram dobit
        slabiji_od_mene /= 2; // medjusobno se ubiju
    }

    return true;
}

bool must_i_win(long long a, long long P) {
    long long bolji_od_mene = a;

    ++P;

    int t = 0;

    for (int i = (N-1); i >= 0; --i) {
        if ((P & (1LL<<i)) == 0) {
            t = 1 + ((N-1) - i);
            if ((P % (1LL<<i)) == 0) { // if of form 1110000
                --t;
            }
            break;
        }
    }

    if (P == (1LL<<N)) return true;
    if (P == ((1LL<<N)-1)) t = N;

    for (int i = 0; i < t; ++i) {
        if (bolji_od_mene == 0) return true;
        bolji_od_mene -= 1;
        bolji_od_mene /= 2;
    }

    return false;
}

int main() {
    int T;
    long long P;
    scanf("%d", &T);

    for (int tt = 1; tt <= T; ++tt) {
        scanf("%d%lld", &N, &P);
        --P; // i look at <= P
        long long max_can = 0;
        long long max_must = 0;

        long long l = 0, r = (1LL<<N); // [l, r>

        while ((r - l) > 1) {
            long long x = (l+r)/2;

            if (must_i_win(x, P)) l = x;
            else r = x;
        }

        max_must = l;

        l = 0; r = (1LL<<N);
        while ((r - l) > 1) {
            long long x = (l+r)/2;

            if (can_i_win(x, P)) l = x;
            else r = x;
        }

        max_can = l;

        /*for (long long a = 0; a < (1LL<<N); ++a) {
            if (must_i_win(a, P)) max_must = a;
            if (can_i_win(a, P)) max_can = a;
        }*/

        printf("Case #%d: %lld %lld\n", tt, max_must, max_can);
    }
    return 0;
}
