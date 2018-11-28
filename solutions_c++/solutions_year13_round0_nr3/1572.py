#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

vector<long> a;

bool ispalin(long n) {
    char s[32];
    sprintf(s, "%ld", n);
    int l = strlen(s);
    reverse(s, s + l / 2);
    return strncmp(s, s + (l + 1) / 2, l / 2) == 0;
}

int main() {
    for (long i = 1; i <= 10000000; ++i) if (ispalin(i) && ispalin(i * i)) a.push_back(i * i);

    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        long A, B;
        scanf("%ld%ld", &A, &B);

        printf("Case #%d: %tu\n", t, upper_bound(a.begin(), a.end(), B) - lower_bound(a.begin(), a.end(), A));
    }

    return 0;
}
