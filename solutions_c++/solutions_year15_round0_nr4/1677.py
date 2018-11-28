#include <stdio.h>
#include <iostream>
#include <fstream>
using namespace std;

int t, x, r, c;

int main(){
    ifstream in;
    in.open("in.txt");
    ofstream out;
    out.open("out.txt");
    in >> t;
    for (int i = 0 ; i < t ; ++i) {
        bool win = true;
        in >> x >> r >> c;
        if ( x == 2 ) {
            if ((r * c) % 2) {
                win = false;
            }
        } else if ( x == 3 ) {
            if ((r * c) % 3) {
                win = false;
            }
            if (r < 2 || c < 2) {
                win = false;
            }
            if (r < 3 && c < 3) {
                win = false;
            }
        } else if ( x == 4 ) {
            if ((r * c) % 4) {
                win = false;
            }
            if (r < 4 && c < 4) {
                win = false;
            }
            if ( r + c < 7) {
                win = false;
            }
        }
        
        out << "Case #" << i + 1 << ": " << (win ? "GABRIEL" : "RICHARD" )  << endl;
    }
    in.close();
    out.close();
}