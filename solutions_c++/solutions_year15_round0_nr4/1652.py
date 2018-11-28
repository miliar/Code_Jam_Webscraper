#include <fstream>
#include <string>

using namespace std;

string solveSmall(int x,int r,int c) {
    if (x == 1) {
        return "GABRIEL";
    }

    if (r > c) swap(r, c);
    if (x == 2) {
        if (r * c % x != 0) return "RICHARD";
        return "GABRIEL";
    } 
    
    if (x == 3) {
        if (r * c % x != 0 || r == 1) return "RICHARD";
        return "GABRIEL";
    } 

    if (x == 4) { 
        if (r * c % 4 != 0) return "RICHARD";
        if (r * c == 4 || r * c == 8) return "RICHARD";   
        // r * c = {12, 16}
        if (r <= 2) return "RICHARD";
        return "GABRIEL";
    }

    return "XX";
}

int main() {
    ifstream cin("test.in");
    ofstream cout("test.out");
    int T;
    cin >> T;
    for (int testCase = 1; testCase <= T; testCase++) {
        int X, R, C;
        cin >> X >> R >> C;
        cout << "Case #" << testCase << ": " << solveSmall(X, R, C) << "\n";
    }

    return 0;
}
