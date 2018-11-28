#include<cstdio>
#include<algorithm>
using namespace std;

const char* calc(int x, int r, int c) {
    if(x == 1)
        return "GABRIEL";
    if(x == 2) {
        if(c >= 2 && (r*c)%2 == 0) return "GABRIEL";
        else return "RICHARD";
    }
    if(x == 3) {
        if (c >= 3 && r >= 2 && (r*c)%3 == 0) return "GABRIEL";
        else return "RICHARD";
    }
    if(x == 4) {
        if(c >= 4 && r >= 3 && (r*c)%4 == 0) return "GABRIEL";
        else return "RICHARD";
    }
}
int main() {
    int Z;
    scanf("%d", &Z);
    for(int zz = 1; zz <= Z; ++zz) {
        int x, r, c;
        scanf("%d %d %d", &x, &r, &c);
        if (c < r) swap(r, c);
        
        printf("Case #%d: %s\n", zz, calc(x, r, c));

    }
    return 0;
}
