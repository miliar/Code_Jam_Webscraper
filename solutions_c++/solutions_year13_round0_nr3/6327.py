#include <cstdio>
#include <cmath>
#include <windows.h>

bool check(long long n) {
    long long sq = (long long) floor(sqrt(n)), rev = 0, sqrev = 0, tmp = n;
    while (tmp) {
        rev *= 10;
        rev += tmp%10;
        tmp /= 10;
    }
    tmp = sq;
    while (tmp) {
        sqrev *= 10;
        sqrev += tmp%10;
        tmp /= 10;
    }
    return (sq*sq == n) && (sq == sqrev) && (n == rev);
}

int main()
{
    FILE *in = fopen("dataC.in", "r"), *out = fopen("dataC.out", "w");
    int T, casenum = 1;
    fscanf (in, "%d", &T);
    while (T--) {
        long long a, b, count = 0;
        fscanf (in, "%lld %lld", &a, &b);
        fprintf (out, "Case #%d: ", casenum++);
        for (long long i = a; i <= b; i++)
            if (check(i)) count++;
        fprintf (out, "%lld\n", count);
    }
    return 0;
}
