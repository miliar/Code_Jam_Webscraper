#include <fstream>
#include <iostream>

using namespace std;

int ovation()
{
    ifstream testcase("example.txt");
    ofstream result("result.out");

    int ncases;
    testcase >> ncases;

    for(int c = 0; c < ncases; ++c) {
        int standing = 0;
        int needed = 0;
        int smax;
        testcase >> smax;
        for(int i=0; i<=smax; ++i) {
            char c;
            testcase >> c;
            int nb = c-'0';
            if(i>standing) {
                needed += i-standing;
                standing += i-standing;
            }
            standing += nb;
        }
        result << "Case #" << c+1 << ": " << needed << endl;

    }
}

int main()
{
    ifstream testcase("example.txt");
    ofstream result("result.out");

    int ncases;
    testcase >> ncases;

    for(int c = 0; c < ncases; ++c) {
        int X, R, C;
        testcase >> X >> R >> C;
        if(((R*C)%X) != 0) {
            result << "Case #" << c+1 << ": RICHARD" << endl;
        } else {
            //cerr << X  << " " << R << " " << C << endl;
            switch(X)
            {
                case 1:
                    result << "Case #" << c+1 << ": GABRIEL" << endl;
                    break;

                case 2:
                    result << "Case #" << c+1 << ": GABRIEL" << endl;
                    break;

                case 3:
                    if((R!=1 && C!=1)) {
                        result << "Case #" << c+1 << ": GABRIEL" << endl;
                    } else {
                        result << "Case #" << c+1 << ": RICHARD" << endl;
                    }
                    break;

                case 4:
                    if(R>2 && C>2)
                    {
                        result << "Case #" << c+1 << ": GABRIEL" << endl;

                    } else {
                        result << "Case #" << c+1 << ": RICHARD" << endl;
                    }
                    break;
            }
        }
    }
}
