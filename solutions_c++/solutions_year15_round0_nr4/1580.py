#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <cmath>

using namespace std;

int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);
    char ans[2][10] = {"GABRIEL", "RICHARD"};
    int t, x, n, m;
    scanf("%d", &t);
    for (int cases = 1; cases <= t; ++cases)
    {
        scanf("%d%d%d", &x, &n, &m);
        if (n > m)
            swap(n, m);
        printf("Case #%d: ",cases);
        if (n <= x - 2) {puts(ans[1]);continue;}
        if (x>6) {puts(ans[1]);continue;}
        if (n < x && m < x) {puts(ans[1]);continue;}
        if ((n * m) % x != 0) {puts(ans[1]);continue;}
        puts(ans[0]);
    }
}
