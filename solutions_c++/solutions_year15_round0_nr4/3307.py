#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>
using namespace std;

int good[5][5][5];

bool solve() {
    int x, r, c;
    cin >> x >> r >> c;

    if(r > c) swap(r,c);

    //printf("%i %i %i\n", r, c, x);

    if((r%2 == 0 || c%2 == 0) && x == 2)
        return true;
    if((x>r) && (x>c))
        return false;
    if(x==1)
        return true;
    if((r*c)%x != 0)
        return false;
    if(x > (r*c)/2)
        return false;

    if(good[r][c][x] == 1) return true;
    if(good[r][c][x] == 2) return false;

    cout << "UNCHECKED: " << r << " " << c << " " << x << endl;
    return false;
}

int main() {
    memset(good, 0, sizeof(good));

    good[1][2][2] = 1;
    good[1][3][3] = 2;
    good[2][3][3] = 1;
    good[2][4][4] = 2;
    good[3][3][3] = 1;
    good[3][3][4] = 2;
    good[3][4][3] = 1;
    good[3][4][4] = 1;
    good[4][4][3] = 2;
    good[4][4][4] = 1;
    

    int t; cin >> t;
    for(int tcase = 1; tcase <= t; ++tcase) {
        printf("Case #%i: ", tcase);
        cout << (solve() ? "GABRIEL" : "RICHARD") << endl;
    }

    return 0;
}
