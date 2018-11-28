#include <set>
#include <stack>
#include <utility>
#include <vector>
#include <queue>
#include <map>
#include <iostream>
#include <cassert>
#include <cmath>
#include <algorithm>
#include <climits>
#include <cassert>

using namespace std;

// return true iff gabriel wins
bool compute_sol(int X, int R, int C) {
    if (X == 1) { // 1 piece
        // gabriel wins no matter what 
        return true;
    }
    if (X == 2) { // 1 piece
        // 1,1 - 3,3 - 1,3 - 3,1 are the only losing grid for gabriel
        if ((R % 2 == 1) && (C % 2 == 1)) { return false;}
        return true;
    }
    if (X == 3) { // 2 pieces
        // at least one dimension = 3
        // 1, 3 false
        // 2, 3 
        // 3, 3
        // 1, 4 false
        // 2, 4 false
        // 3, 4
        // 4, 4 false
        if (R == 2 && C == 3) { return true;} 
        if (R == 3 && C == 2) { return true;} 
        if (R == 3 && C == 3) { return true; }
        if (R == 3 && C == 4) { return true; }
        if (R == 4 && C == 3) { return true; }
        return false;
    }
    if (X == 4) {
        // at least one dimension = 4 G loses as R will chose a 4-bar
        // 1,4   G loses coz R will chose a square
        // 2,4   G loses coz R will chose a T
        // 3,4   G win 
        // 4,4   G win
        if (R == 4 && C == 4) { return true; } 
        if (R == 4 && C == 3) { return true; }
        if (R == 3 && C == 4) { return true; }
        return false;
    }
   return true;
}

int main()  {
    int T;

    scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        int X, R, C;
        scanf("%d %d %d", &X, &R, &C);
        assert(X <= 4 && R <= 4 && C <= 4);
        bool res = compute_sol(X,R,C); 
        printf("Case #%d: %s\n", i+1, res?"GABRIEL":"RICHARD");
    }

    return 0;
}

 
