#include <iostream>


using namespace std;


int main(int argc, char** argv) {

    int T;
    cin >> T;
    for (int cases = 1; cases <= T; ++cases) {
    int X, R, C;
    cin >> X >> R >> C;
    
    string ans = "GABRIEL";
    
    if (R*C % X != 0) ans = "RICHARD";
    
    if (X == 3 && (R==1 || C == 1)) ans = "RICHARD";
    
    if (X == 4){
        if (R == 1 || C == 1) ans = "RICHARD";
        if (R == 2 && C == 2) ans = "RICHARD";
        if (R == 2 && C == 4) ans = "RICHARD";
        if (R == 4 && C == 2) ans = "RICHARD";
    }
    cout << "Case #" << cases << ": " << ans << endl;
    }
    return 0;
}

