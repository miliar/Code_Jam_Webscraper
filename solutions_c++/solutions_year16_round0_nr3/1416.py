#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <map>
using namespace std;

unsigned long long mod = 304250263527210uLL;

map<unsigned long long, bool> mp;

int s[33];
int p[11];

int n = 32, k = 500;

int get(unsigned long long x) {
    for (int i = 2; i <= 41 && i < x; ++i) if (x % i == 0) return i;
    return 0;
}

bool check() {
    unsigned long long x;
    for (unsigned long long i = 2; i <= 10; ++i) {
        x = 0;
        for (int j = 1; j <= n; ++j) x = (x * i + s[j]) % mod;
        p[i] = get(x);
        if (p[i] == 0) return false;
    }
    if (mp.count(x)) return false;
    mp[x] = true;
    return true;
}

bool solve() {
    unsigned int x = rand();
    for (int i = 2; i < n; ++i) s[i] = x % 2, x /= 2;
    if (check()) {
        for (int i = 1; i <= n; ++i) printf("%d", s[i]);
        for (int i = 2; i <= 10; ++i) printf(" %d", p[i]);
        puts("");
        return true;
    }
    return false;
}

int main()
{
    //freopen("c.in", "r", stdin);
    freopen("c_output.txt", "w", stdout);

    s[1] = s[n] = 1;
    srand(time(NULL));
    puts("Case #1:");
    while (k) {
        if (solve()) --k;
    }

    return 0;
}
