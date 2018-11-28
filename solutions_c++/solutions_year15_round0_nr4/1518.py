#include <iostream>
#include <set>
#include <string>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <fstream>

using namespace::std;


void fourth() {
    ifstream file("D-small-attempt1.in");
    ofstream out("fourth.out");
    size_t t;
    file >> t;
    for (size_t case_ = 1; case_ <= t; ++case_) {
        int X, R, C;
        string answer = "GABRIEL";
        file >> X >> R >> C;
        if (C < R) {
            swap(C, R);
        }
        if ((R * C) % X != 0 || C < X) {
            answer = "RICHARD";
        }
        else if (X == 3) {
            if (R == 1) {
                answer = "RICHARD";
            }
        }
        else if (X == 4) {
            if (R ==1) {
               answer = "RICHARD";
            }
            if (R == 2) {
                answer = "RICHARD";
            }
        }
        cout << "Case #" << case_ <<": " << answer << endl;
    }

}


int main(int argc, const char* argv[]) {
    fourth();
    return 0;    
}