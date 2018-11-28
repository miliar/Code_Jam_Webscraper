//
//  OminousOmino.cpp
//  OminousOmino
//

#include <iostream>
#include <fstream>
#include <string>

int main(int argc, const char * argv[]) {
    int T, count = 1;
    int X;
    int R;
    int C;
    int A;
    int B;
    int gridArea;
    std::string winner;
    freopen("/Users/Michael/Desktop/D-small-attempt6.in", "r", stdin);
    std::ofstream outs("/Users/Michael/Desktop/output");
    scanf("%i", &T);
    while (T--) {
        outs << "Case #" << count << ": ";
        scanf("%i%i%i", &X, &R, &C);
        gridArea = R * C;
        if (R > C) {
            A = R;
            B = C;
        } else {
            A = C;
            B = R;
        }
        if (X >= 7) {
            winner = "RICHARD";
        }
        else if ((X < 3) && (X == gridArea)) {
            winner = "GABRIEL";
        }
        else if (X == 1 && gridArea > 1) {
            winner = "GABRIEL";
        }
        
        
        else if (X > gridArea) {
            winner = "RICHARD";
        }
        else if (gridArea % X != 0) {
            winner = "RICHARD";
        }
        else if ((X > 2) && (X >= B * 2)) {
            winner = "RICHARD";
        }
        else {
            winner = "GABRIEL";
        }
        
        
        outs << winner << "\n";
        count++;
    }
    
    return 0;
}
