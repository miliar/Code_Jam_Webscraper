#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std;

bool cmp(double a, double b)
{
    return a>b;
}

double a[1111], b[1111];

int main()
{
    int testcase, p1, n, p2, score1, score2;
    freopen("warL.in", "r", stdin);
    freopen("warL.out", "w", stdout);
    scanf("%d", &testcase);
    for (int test = 1; test <= testcase; test++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++) scanf("%lf", &a[i]);
        for (int i = 0; i < n; i++) scanf("%lf", &b[i]);
        sort(a, a+n, cmp);
        //for (int i = 0; i < n; i++) printf("%lf ", a[i]);printf("\n");
        sort(b, b+n, cmp);
        //for (int i = 0; i < n; i++) printf("%lf ", b[i]);printf("\n");
        score1 = 0;
        p1 = n-1; p2 = n-1;
        while (p1 >= 0 && p2 >= 0) {
            while (p1 >=0 && a[p1] < b[p2])
                p1--;
            if (p1 < 0) break;
            score1++;
            p1--;p2--;
        }

        p1 = n-1; p2 = n-1;
        score2 = 0;
        while (p1 >= 0 && p2 >= 0) {
            while (p2 >= 0 && b[p2] < a[p1]) {
                p2--;
            }
            if (p2 < 0) break;
            score2++;
            p2--;p1--;
        }
        score2 = n - score2;
        printf("Case #%d: %d %d\n", test, score1, score2);
    }
    return 0;
}
