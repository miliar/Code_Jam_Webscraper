#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream f("D-small-attempt2.in");
    ofstream g("outputomino2.txt");
    int T;
    f >> T;
    for (int i=0;i<T;++i) {
        int X, R, C;
        string gyoztes;
        f >> X >> R >> C;
        if (R < X && C < X)
            gyoztes = "RICHARD";
        else if (R*C % X != 0)
            gyoztes = "RICHARD";
        else if (X == 3 && (R == 1 || C == 1))
            gyoztes = "RICHARD";
        else if (X == 4) {
            if ((R == 3 && C == 4) || (R == 4 && C == 3) || (R == 4 && C == 4)) gyoztes = "GABRIEL";
            else gyoztes = "RICHARD";
        }
        else gyoztes = "GABRIEL";

        g << "Case #" << (i+1) << ": " << gyoztes << endl;
    }
    return 0;
}
