#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char const *argv[])
{
    int tests, case_num = 0;
    ifstream input ("D-small-attempt2.in");
    input >> tests;
    while (tests--)
    {
        int x, r, c, half;
        input >> x >> r >> c;
        if (x % 2 == 0)
            half = x / 2;
        else
            half = (x / 2) + 1;
        if ((r * c) < x || (x > c && x > r) || (half > r || half > c) || ((r * c) % x != 0) || (x == 4 && (c == x / 2 || r == x / 2)))
        {
            cout << "Case #" << ++case_num << ": RICHARD" << endl;
            //cout << " ( " << x << " " << r << " " << c << " )" << endl;
        }
        else
        {
            cout << "Case #" << ++case_num << ": GABRIEL" << endl;
            //cout << " ( " << x << " " << r << " " << c << " )" << endl;
        }
    }
    input.close();
    return 0;
}