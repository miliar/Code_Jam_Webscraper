#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <set>
#include <string>

using namespace std;

typedef long long LL;
const int maxn = 1e7 + 1;
int cnt[maxn], l;
char str[maxn];
LL list[maxn];

bool check1() {
    int len = strlen(str);
    for (int i = 0; i < len / 2; ++i) {
        if (str[i] != str[len - i - 1]) return false;
    }
    return true;
}

bool check(LL i) {
    sprintf(str, "%lld", i);
    if (!check1()) return false;
    sprintf(str, "%lld", i * i);
    if (!check1()) return false;
    return true;
}

void init() {
    l = 0;
    for (LL i = 1; i < maxn; ++i) {
        list[i] = i * i;
        cnt[i] = cnt[i - 1];
        if (check(i)) ++cnt[i];
    }
}

void solved(int nT) {
    LL A, B;
    scanf("%lld %lld", &A, &B);
    printf("Case #%d: ", nT);
    int p1 = lower_bound(list, list + maxn, A) - list;
    int p2 = upper_bound(list, list + maxn, B) - list - 1;
    printf("%d\n", cnt[p2] - cnt[max(0, p1 - 1)]);
}

int main() {
    freopen("C-large-1.in", "r", stdin);
    freopen("C-large-1.out", "w", stdout);
    init();
    int T = 1;
    scanf("%d", &T);
    for (int nT = 1; nT <= T; ++nT) {
        solved(nT);
    }
    return 0;
}