#include <cstdio>
#include <cmath>
#include <vector>
using namespace std;

int ispal(long long n) {
    long long u = 0;
    long long x = n;
    while (x)
        u = u * 10 + (x % 10),
        x /= 10;
    if (u == n)
        return 1;
    return 0;
}
int isOk(long long n) {
    if (ispal(n) && ispal(n * n))
    {
//        printf (":::%lld - %lld\n", n, n * n);
        return 1;
    }
    return 0;
}
vector<long long> s;
int main() {

    int rz = 0, x = 10;
    long long i , N = 10000000;
    for (i = 1; i <= N; ++i) {
        if (isOk(i))
            s.push_back(i * i);
    }
    int T;
    freopen ("c.in", "r", stdin);
    freopen ("c.out", "w", stdout);
    scanf ("%d", &T);
    for (int test = 1; test <= T; ++test) {
        long long a, b;
        scanf ("%lld %lld", &a, &b);
        int i;
        int nr = 0;
        for (i = 0; i < s.size(); ++i)
            if (a <= s[i] && s[i] <= b) {
                ++nr;
            }
        printf ("Case #%d: %d\n", test, nr);
    }
}
