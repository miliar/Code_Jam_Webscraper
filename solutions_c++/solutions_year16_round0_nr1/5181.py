#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair

#define eps 0.0000001
#define pi  3.14159265359
#define inf 2000000000

typedef long long lld;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;

bool mark[10];

bool marked_all() {
    for (int i = 0; i < 10; i++)
        if (!mark[i]) return false;
    return true;
}

void mark_one(long long x) {
    while (x > 0) {
        mark[x % 10] = true;
        x /= 10;
    }
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int tt;
    long long n;
    scanf("%d", &tt);
    for (int i = 1; i <= tt; i++) {
        scanf("%lld", &n);
        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", i);
            continue;
        }
        for (int j = 0; j < 10; j++) mark[j] = false;
        mark_one(n);
        long long curr = 1;
        while (!marked_all()) {
            curr++;
            mark_one(curr * n);
        }
        printf("Case #%d: %lld\n", i, curr * n);
    }
    return 0;
}
