#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

#define MAX 1005
int pancakes[MAX];

// ------------- global -------------

// ------------- functions -------------

// ------------- main -------------
int main () {
    int T;
    cin >> T;
    
    for(int i=0; i<T; i++){
        int X, R, C;
        cin >> X >> R >> C;
        
        bool richWins = false;
        int min = (R < C ? R : C),
            max = (R > C ? R : C);
        if(X > 6 || R*C % X != 0 || (X+1)/2 > min || (X > 3 && min <= 2))
            richWins = true;
        //cout << X << " " << R << " " << C << " " << (richWins ? "R" : "G") << endl;
        cout << "Case #" << (i+1) << ": " << (richWins ? "RICHARD" : "GABRIEL") << endl;
    }

    return 0;
}
