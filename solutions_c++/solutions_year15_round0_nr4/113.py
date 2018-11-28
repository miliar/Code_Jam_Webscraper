#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <algorithm>
using namespace std;
int X, R, C;
bool contain(int X, int R, int C) {
    if (X > C)
        return false;
    if (X <= C)
        return true;
    return false;
}
bool solve() {
    if (R * C % X != 0)
        return false;
    assert(R <= C);

    if (X == 1)
        return true;
    if (X == 2)
        return true;
    if (X >= 7)
        return false;
    if (X > C)
        return false;
    if (C == 1)
        return true;
    if (X >= 2 * R)
        return false;
    if (contain(X, R - 2, C - 2))
        return true;

if (X==3 && R==2 && C==3) return true;
if (X==3 && R==3 && C==3) return true;
if (X==3 && R==3 && C==4) return true;
if (X==4 && R==3 && C==4) return true;
if (X==4 && R==4 && C==4) return true;
if (X==4 && R==4 && C==5) return true;
if (X==5 && R==3 && C==5) return false;
if (X==5 && R==4 && C==5) return true;
if (X==5 && R==5 && C==5) return true;
if (X==5 && R==5 && C==6) return true;
if (X==6 && R==4 && C==6) return true;
if (X==6 && R==5 && C==6) return true;
if (X==6 && R==6 && C==6) return true;
if (X==6 && R==6 && C==7) return true;

    return true;
}
int main(){
    int T, Tt, i;
    scanf("%d", &T);
    for (X = 1; X < 300; ++X) {
        for (C = 1; C < 300; ++C) {
            for (R = 1; R <= C; ++R) {
                solve();
            }
        }
    }
    for (Tt = 1; Tt <= T; ++Tt) {
        scanf("%d%d%d", &X, &R, &C);
        if (R > C)
            swap(R, C);
        printf("Case #%d: %s\n", Tt, solve() ? "GABRIEL" : "RICHARD");
    }
    return 0;
}
