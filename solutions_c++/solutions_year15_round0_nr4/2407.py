#include <iostream>
#include <cmath>

using namespace std;

int main(){
    int t;
    cin >> t;
    for(int u = 1; u <= t; u++){
        // x-omino
        // r by c board
        int x, r, c;
        cin >> x >> r >> c;
        int sq = (int) sqrt(x);
        string winner = "GABRIEL";
        if(r < x && c < x){
            winner = "RICHARD";
            // choose straight omino
            // can't fit on board
        }
        else if(sq > r || sq > c){
            winner = "RICHARD";
        }

        else if((r * c) % x != 0){
            winner = "RICHARD";
            // can never fill a board exactly
        }
        else if(x >= 7){
            winner = "RICHARD";
            // make a hole in the middle, eg
            // ooo
            // o o
            // oo
        }
        else if(x == 4 && ((r == 2 && c == 4) || (r == 4 && c == 2))){
            winner = "RICHARD";
            // hard coded richard win for
            // o
            // oo
            // o
        }
        else if(x == 3 && (r == 1 || c == 1)){
            winner = "RICHARD";
            // hard coded richard win for
            // o
            // oo
        }

        cout << "Case #" << u << ": " << winner << endl;
    }

    return 0;
}
