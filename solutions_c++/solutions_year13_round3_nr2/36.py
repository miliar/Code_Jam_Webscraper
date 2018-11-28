#include <iostream>

using namespace std;

string solve (){
    int x, y;
    string res;
    cin >> x >> y;

    string yDir = "SN", xDir = "WE";

    if ( y < 0 ){
        swap ( yDir[0], yDir[1] );
        y *= -1;
    }
    if ( x < 0){
        swap ( xDir[0], xDir[1] );
        x *= -1;
    }

    for ( int i = 0; i < x; ++ i )
        res += xDir;

    for ( int i = 0; i < y; ++i )
        res += yDir;

    return res;
}
int main(){
    int tests;

    cin >> tests;

    for ( int i = 1; i <= tests; ++i )
        cout << "Case #" << i << ": " << solve()<< endl;
}
