#include <cstdio>
#include <iostream>
#include <map>
#include <vector>
#include <queue>
#include <cstring>
using namespace std;

double c, f, x;
int main() {
    freopen("D:\\data.in", "r", stdin);
    freopen("D:\\data.out", "w", stdout);
    int cas, t = 0;
    cin >> cas;
    while (cas--) {
        cin >> c >> f >> x;
        double rate = 2, total = x / rate, ans = x / rate;
        for (int i = 1; i < x; i++) {
            total += (c - x) / rate + x / (rate + f);
            rate += f;
            ans = min(total, ans);
        }
        printf("Case #%d: %.7lf\n", ++t, ans);
    }
    return 0;
}