#include <iostream>
#include <cassert>
#include <vector>
#include <algorithm>
using namespace std;

int main(int argc, char **args) {
    int num_cases;
    cin >> num_cases;

    for(int case_num=0; case_num < num_cases; case_num++) {
        bool possible = false;

        int X, R, C;
        cin >> X >> R >> C;

        // If the grid can't fit a multiple of N, then obviously not a win; don't calculate
        // If we can exceed the height or width, obvious win
        if(R*C % X == 0) {
            // Else, do the math
            // If we can select an ominoe so that X-1 > R or C, it's not possible
            if(X-1 > R || X-1 > C)
                possible = false;
            // As long as there are no x-ominoes that completely enclose an area
            //  it is possible
            else if(X < 8)
                possible = true;
        }

        cout << "Case #" << (case_num+1) << ": " << (!possible ? "RICHARD" : "GABRIEL")  << endl;
    }

    return 0;
}
