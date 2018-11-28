#include <iostream>
#include <algorithm>
using namespace std;

int x, r, c;

int two(){
    if ((r * c) % 2 == 0) return 1;
    return 0;
}
int three(){
    if ((r * c) % x != 0) return 0;
    if (r < 2 || c < 3) return 0;
    if (r == 2 && c == 3) return 1;
    if (r == 3 && c == 3) return 1;
    if (r == 3 && c == 4) return 1;
    //if (r == 4 && c == 4) return
    return 0;
}
int four(){
    if ((r * c) % x != 0) return 0;
    if (r < 3 || c < 4) return 0;
    if (r == 3 && c == 4) return 1;
    if (r == 4 && c == 4) return 1;
    return 0;
}
int solve(){
    if (x == 1) return 1;
    if (x == 2) return two();
    if (x == 3) return three();
    if (x == 4) return four();
    return 0;
}
int t;

void FileIO(){
    freopen("ac.in", "r", stdin);
    freopen("ac.out", "w", stdout);
}

int main(){
    FileIO();
    scanf("%d", &t);
    for (int i = 1; i <= t; ++i){
        scanf("%d%d%d", &x, &r, &c);
        if (r > c) swap(r, c);
        if (solve()) printf("Case #%d: GABRIEL\n", i);
        else printf("Case #%d: RICHARD\n", i);
    }
    return 0;
}
