#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int main()
{
    freopen("C:\\Users\\pranjuldb\\Desktop\\a.in", "r", stdin);
    freopen("C:\\Users\\pranjuldb\\Desktop\\b.out", "w", stdout);
    int t, i, j, k, a, b;
    scanf("%d", &t);
    int cases = 1;
    while (t--) {
        int ctr = 0;
        scanf("%d%d%d", &a, &b, &k);
        for (i = 0; i < a; i++) {
            for (j = 0; j < b; j++) {
                if ((i&j) < k) {
                    ctr++;
                }
            }
        }
        printf("Case #%d: %d\n", cases, ctr);
        cases++;
    }
    return 0;
}
