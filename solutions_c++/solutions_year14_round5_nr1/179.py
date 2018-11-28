#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;

const int maxn = 1000002;
double sum[maxn];
int n, p, q, r, s;

void update(double &ans, int f, int r) {
    double mm = max(sum[f], max(sum[r] - sum[f], sum[n] - sum[r]));
    double nans =  1 - mm / sum[n];
    ans = max(ans, nans);
}

double solve() {

    scanf("%d%d%d%d%d", &n, &p, &q, &r, &s);
    sum[0] = 0;
    for (long long i = 0; i < n; ++i)
        sum[i+1] = ((i * p + q) % r + s) + sum[i];
    int f = 0;
    double ans = 0;

    for (int r = 1; r <= n; ++r) {
        update(ans, f, r);
        long long thr = sum[r] / 2;
       // for (int j = 0; j < r; ++j) update(ans, j, r);
        while (f + 1 < r && sum[f] < thr) {
            f++;
            update(ans, f, r);
        }
        if (f > 0) f--;
    }
    return ans;
}

int main()
{
    freopen("D:\\work\\gcj14\\r4\\cppinput.txt", "r", stdin);
    freopen("D:\\work\\gcj14\\r4\\cppoutput.txt", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; ++i) {
        printf("Case #%d: %.10f\n", i,  solve());
    }
    fprintf(stderr, "done\n");
    return 0;
}

