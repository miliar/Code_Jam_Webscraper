#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;
#define INPUT "A-small-attempt3.in"

int main()
{
    ifstream in;
    ofstream out;
    in.open(INPUT);
    out.open("out.txt");
    int T = 0;
    in >> T;
    int cards[4];
    int row, a;
    
    for (int t = 0; t < T; ++t) {
        out << "Case #" << t+1 << ": ";
        string y = "Volunteer cheated!";

        in >> row;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                if (i == row-1)
                    in >> cards[j];
                else in >> a;
            }
        }
        
        in >> row;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                in >> a;
                if (i == row-1) {
                    for (int k = 0; k < 4; ++k) {
                        if (cards[k] == a) {
                            ostringstream convert;
                            convert << a;
                            y = y == "Volunteer cheated!" ?
                                        convert.str() : "Bad magician!";
                        }
                    }
                }
            }
        }
        out << y << endl;
    }
    return 0;
}

