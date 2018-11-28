//
//  main.cpp
//  Ominous Omino
//

#include <iostream>
#include <bitset>
#include <vector>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
    freopen("D-small-attempt0.in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T, pid = 1;
    for (cin>>T; T--;) {
        cout << "Case #" << pid++ <<": ";
        int X, R, C;
        cin >> X >> R >> C;
        int sX = ceil(sqrt(X));
        if (X <= 2) {
            if (R*C < X || R*C % X != 0) cout << "RICHARD\n";
            else cout << "GABRIEL\n";
        } else {
            if (R*C <= X || (R < sX || C < sX) || R*C % X != 0) cout << "RICHARD\n";
            else if (4 == X && ((R == 2 && C == 4) || (R == 4 && C == 2))) cout << "RICHARD\n";
            else cout << "GABRIEL\n";
        }
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
