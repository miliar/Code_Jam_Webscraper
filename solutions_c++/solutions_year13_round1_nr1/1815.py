#include <iostream>
#include <fstream>

using namespace std;

int main(void)
{
    ifstream inp("A-small-attempt0.in", ifstream::in);
    ofstream out("result"  , ofstream::out);

    int tcs = 0;
    inp >> tcs;

    for ( int i = 1; i<=tcs; i++ ) {
        long long r,t;
        long long count = 0;

        inp >> r >> t;
        while ( 1 ) {
            t -= (2*r+1);
            if ( t < 0 ) break; //Last rig not possible.
            count++;
            r+=2;
        }
        
        cout << "Case #" << i << ": " << count << endl;
        out << "Case #" << i << ": " << count << endl;
    }

    return 0;
}
