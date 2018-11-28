#include <iostream>
#include <cstdio>
using namespace std;

double table[100001];

int main() {
    int T;
    double c, f, x;
    cin>>T;
    for (int tc = 1; tc <= T; ++tc) {
        cin>>c>>f>>x;
        table[0] = 0;
        for (int i = 1; i < 100001; ++i)
            table[i] = table[i-1] + c / (2.0 + f * (i - 1));
        for (int i = 0; i < 100001; ++i)
            table[i] += x / (2.0 + f * i);

        double ans = 1e10;
        for (int i = 0; i < 100001; ++i)
            ans = min(ans, table[i]);

        printf("Case #%d: %.10f\n", tc, ans);
    }
}
