#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

const int N = 1005;
int p[N];

int main () {
//    freopen("B-large.in", "r" ,stdin);
//    freopen("out.txt", "w", stdout);
    int cases;
    cin >> cases;
    int D;
    for (int cas = 1; cas <= cases; cas ++) {
        scanf ("%d", &D);
        int x = 0;
        for (int i = 0; i < D; i++) {
            scanf ("%d", &p[i]);
            if (x < p[i]) {
                x = p[i];
            }
        }
        int ans = x;
        for (int i = 1; i <= x; i++) {
            int num = 0;
            for (int j = 0; j < D; j++) {
                if (p[j] > i) {
                    num += (p[j] - 1) / i;
                }
            }
            ans = min(ans, num + i);
        }


        printf ("Case #%d: %d\n", cas, ans);
    }

    return  0;
}
