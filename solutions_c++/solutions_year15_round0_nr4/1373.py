#include<stdio.h>
#include<string.h>
#include<algorithm>
int X, R, C;
bool out() {
    // 1 * ?
    if(X > C) {
        return true;
    }
    // 2 * ?
    if(X >= 3) {
        if(R < 2 || X - 1 > C) {
            return true;
        }
    }
    // 3 * ?
    if(X >= 5) {
        if(R < 3 || X - 2 > C) {
            return true;
        }
    }
    return false;
}
bool split() {
    int n = X - R;
    for(int i = 0; i <= n; i ++) {
        bool ok = false;


        if(!ok) {
            return true;
        }
    }
    return false;
}
bool win() {
    if(R > C) {
        std::swap(R, C);
    }
    if(X >= 7) {
        return true;
    }
    if(R * C % X != 0) {
        return true;
    }
    if(out()) {
        return true;
    }
    if(X >= R + C - 1) {
        return true;
    }
    if(X >= 5 && R > 3 && X >= R + C - 3 ) {
        return true;
    }
    if(X >= 5 && X >= R + C - 2) {
        return true;
    }
    if(X >= R + R - 1) {
        if(split()) {
            return true;
        }
    }
    return false;
}
bool winSmall() {
    if(R > C) {
        std::swap(R, C);
    }
    if(R == 1 && C == 1) {
        return X == 2 || X == 3 || X == 4;
    }
    if(R == 1 && C == 2) {
        return X == 3 || X == 4;
    }
    if(R == 1 && C == 3) {
        return X == 2 || X == 3 || X == 4;
    }
    if(R == 1 && C == 4) {
        return X == 3 || X == 4;
    }
    if(R == 2 && C == 2) {
        return X == 3 || X == 4;
    }
    if(R == 2 && C == 3) {
        return X == 4;
    }
    if(R == 2 && C == 4) {
        return X == 3 || X == 4;
    }
    if(R == 3 && C == 3) {
        return X == 2 || X == 4;
    }
    if(R == 3 && C == 4) {
        return false;
    }
    if(R == 4 && C == 4) {
        return X == 3;
    }
    return false;
}
int main() {
    //freopen("input.txt", "rb", stdin);
    freopen("D-small-attempt3.in", "rb", stdin);
    freopen("output.txt", "wb", stdout);
    int t;
    scanf("%d", &t);
    for(int tt = 1; tt <= t; tt ++) {
        scanf("%d%d%d", &X, &R, &C);
        printf("Case #%d: %s\n", tt, winSmall() ? "RICHARD" : "GABRIEL");
    }
    return 0;
}
