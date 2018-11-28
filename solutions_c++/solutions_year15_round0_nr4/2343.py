#include <iostream>
#include <math.h>

using namespace std;

void richard(int c) {
    cout << "Case #" << c << ": " << "RICHARD" << endl;
}

void gabriel(int c) {
    cout << "Case #" << c << ": " << "GABRIEL" << endl;
}

int main() {
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
       int X, R, C;
       cin >> X >> R >> C;
       
       if(R * C % X != 0) {
           richard(t);
           continue;
       }
       if(X > max(R, C)) {
           richard(t);
           continue;
       }
       if((X / 2 + X % 2) > min(R, C)) {
           richard(t);
           continue;
       }
       if(X == 2 || X == 3) {
           gabriel(t);
           continue;
       }
       if(X == 4 && (R == 2 || C == 2)) {
            richard(t);
            continue;
       }
       gabriel(t); 
    }
    return 0;
}
