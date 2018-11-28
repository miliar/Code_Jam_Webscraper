#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int bad(int msk, int R, int C) {
    int bd = 0;
    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            if (i < R - 1) {
                if (msk & (1 << (i * C + j)) && msk & (1 << ((i + 1) * C + j))) {
                    ++bd;    
                }
            }
            if (j < C - 1) {
                 if (msk & (1 << (i * C + j)) && msk & (1 << (i * C + j + 1))) {
                    ++bd;    
                }
           
            }    
        }
    }
    return bd;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int test = 1; test <= T; ++test) {
        int res = 100000;
        int R, C, N;
        scanf("%d%d%d", &R, &C, &N);
        for (int mask = 0; mask <= (1 << R*C); ++mask) {
            if (__builtin_popcount(mask) == N && bad(mask, R, C) < res){
                res = bad(mask, R, C);
            }
        }
        printf("Case #%d: %d\n", test, res);
    }
}