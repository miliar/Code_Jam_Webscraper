# include <iostream>
# include <cstdio>
# include <cstring>

using namespace std;

bool solve(int x,int r,int c) {
    if(r * c % x) return false;
    if(r > c) swap(r, c);
    if(x == 1) return true;
    if(x == 2) return true;
    if(x == 3) return (r >= 2 && c >= 3);
    if(x == 4) return (r >= 3 && c >= 4);
    while(1);
}

int main() {
    int T; cin >> T;
    int cas = 0;
    while(T--) {
        int x, R, C;
        scanf("%d%d%d", &x, &R, &C);
        printf("Case #%d: ", ++cas);
        if(solve(x, R, C))
            puts("GABRIEL");
        else
            puts("RICHARD");
    }
}

