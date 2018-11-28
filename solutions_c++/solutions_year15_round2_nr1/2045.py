#include <iostream>
#include <cstdio>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <vector>
#include <cmath>
#include <queue>
#include <functional>
#include <algorithm>

#define LL long long
#define FOR(i, n) for(int i=0;i<(n);i++)
#define For(i, a, n) for(int i=(a);i<(n);i++)
#define pb push_back
#define MKP make_pair
#define PII pair<int, int>
#define PLL pair<LL, LL>
#define VI vector<int>
#define VL vector<LL>
#define VB vector<bool>
#define VVI vector< VI >
#define VVL vector< VL >
#define VVB vector< VB >
#define range(x) x.begin(), x.end()
#define cc continue

using namespace std;

LL rev(LL wh) {
    LL ret = 0;
    if (wh % 10 == 0) return 0LL;
    while (wh) {
        ret *= 10;
        ret += wh % 10;
        wh /= 10;
    }
    return ret;
}

int main()
{

    int T; scanf("%d", &T);
    FOR(l, T) {
        LL sum = 0;

        LL N; scanf("%lld", &N);
        queue< PLL > Q; Q.push(MKP(N, 1));

        VI A(N, -1);
        while (!Q.empty()) {
            PLL p = Q.front(); Q.pop();
            //printf("%lld %lld\n", p.first, p.second);
            if (p.first == 1) {sum = p.second; break;}
            if (p.first < 1) cc;

            if (A[p.first-1] > -1) cc;
            A[p.first-1] = p.second;

            if (rev(p.first) < p.first) Q.push(MKP(rev(p.first), p.second+1));
            Q.push(MKP(p.first-1, p.second+1));
        }

        printf("Case #%d: %lld\n", l+1, sum);
    }

    return 0;
}
