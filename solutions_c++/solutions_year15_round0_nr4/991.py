#include <cstdio>
#include <algorithm>
#include <iostream>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <cstring>
using namespace std;

#define N 1005
#define MII map<int, int>
#define ITER_MII map<int, int>::iterator

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int kase, x, r, c;

    scanf("%d", &kase);
    for (int kase_no = 1; kase_no <= kase; kase_no++) {
        scanf("%d%d%d", &x, &r, &c);
        if (r * c % x != 0 || r * c < x)
            printf("Case #%d: RICHARD\n", kase_no);
        else {
            // r * c = kx (k >= 2)
            if (x <= 2)
                printf("Case #%d: GABRIEL\n", kase_no);
            else if (x == 3) {
                if (r == 1 || c == 1)
                    printf("Case #%d: RICHARD\n", kase_no);
                else
                    printf("Case #%d: GABRIEL\n", kase_no);
            }
            else {
                if (r <= 2 || c <= 2)
                    printf("Case #%d: RICHARD\n", kase_no);
                else
                    printf("Case #%d: GABRIEL\n", kase_no);
            }
        }
    }
    return 0;
}
