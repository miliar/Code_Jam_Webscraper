#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
#define OUT(x) cerr << #x << ": " << (x) << endl
#define SZ(x) ((int)x.size())
#define FOR(i, n) for (int i = 0; i < (n); ++i)
using namespace std;
typedef long long LL;

bool fair(LL x) {
    int a[32], la = 0;
    while (x) a[la++] = x % 10, x /= 10;
    int i = 0, j = la - 1;
    while (i < j && a[i] == a[j]) ++i, --j;
    return i >= j;
}

int main() {
    vector<LL> v;
    for (LL i = 1; i <= 10 * 1000 * 1000; ++i)
        if (fair(i) && fair(i * i)) v.push_back(i * i);
    int T;
    LL A, B;
    scanf("%d", &T);
    for (int id = 1; id <= T; ++id) {
        scanf("%lld%lld", &A, &B);
        int ans = upper_bound(v.begin(), v.end(), B) - lower_bound(v.begin(), v.end(), A);
        printf("Case #%d: %d\n", id, ans);
    }
    return 0;
}
