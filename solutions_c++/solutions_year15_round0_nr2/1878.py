#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int P[3000];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int test = 1; test <= T; ++test) {
        int D;
        scanf("%d", &D);
        int opt = 0;
        int res = 0;
        for(int i = 0; i < D; ++i) {
            scanf("%d", &P[i]);
            opt = max(P[i], opt);
        }
        res = opt;
        for (int i = 1; i < opt; ++i) {
            int sum = i;
            for (int j = 0; j < D; ++j) {
                sum += P[j]/i + (P[j] % i != 0) - 1;    
            }
            res = min(res, sum);
        } 
        printf("Case #%d: %d\n", test, res);
    }
}