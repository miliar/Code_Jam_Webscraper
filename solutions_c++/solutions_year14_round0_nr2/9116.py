/*
    https://code.google.com/codejam/contest/2974486/dashboard#s=p1
*/
#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    int T;
    double C, F, X;
    
    cin >> T;
     
    for (int i = 1; i <= T; i++) {
        cin >> C;
        cin >> F;
        cin >> X;
        
        double P = 2.0;
        double toC = 0.0;
        double toX = 0.0;
        double minToC = 99999999999.0;
        while(true) {
            toX = toC + (X / P);
            toC += (C / P);
         
            if (minToC > toX)
                minToC = toX;
            else
                break;
            P += F;
        }
        
        printf("Case #%d: %1.7f\n", i, minToC);
    }
    
    return 0;
}
