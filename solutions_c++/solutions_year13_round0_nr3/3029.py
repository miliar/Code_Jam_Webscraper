#include <iostream>
#include <sstream>
#include <fstream>
#include <cmath>

using namespace std;

bool isPol(int x)
{
    stringstream str;
    str << x;

    for ( int i = 0 ; i < str.str().length(); i++ ) {
        if (str.str()[i] != str.str()[str.str().length()-1-i]) {
            return false;
        }
    }

    return true;
}

bool isFairPol(int x)
{
    //check if we have an integer sqrt.
    int sq = sqrt(x);
    if (sq * sq != x) {
        return false;
    }

    //check if x is pol
    if (!isPol(x)) {
        return false;
    }

    //check if the sqrt is pol
    if (!isPol(sq)) {
        return false;
    }

    return true;
}

int main(void)
{
    ifstream inp("C-small-attempt0.in", ifstream::in);
    ofstream out("test.out", ofstream::out);

    int tcs;

    inp >> tcs;

    for ( int tc = 0 ; tc < tcs; tc++ ) {
        int a,b,res = 0;
        inp >> a >> b;
        for ( int act = a ; act <= b; act++ ) {
            if (isFairPol(act)) {
                res++;
                cout << act << " is FP." << endl;
            }
        }
        cout << "Case #" << tc+1 << ": " << res << endl;
        out << "Case #" << tc+1 << ": " << res << endl;
    }

    return 0;    
}
