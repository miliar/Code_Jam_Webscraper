#include <iostream>
#include <fstream>
#include <list>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int main()
{
    ifstream in("A-small-attempt1.in");
    ofstream out("output.out");

    int T;
    in >> T;

    for( int t = 1; t <= T; t++ )
    {
        out << "Case #" << t << ": ";

        int Smax, n;
        in >> Smax >> n;

        int S = 0;
        int guests = 0;
        int d;
        for( int k = 0; k <= Smax ; k++ )
        {
            S += ((int)(n/pow(10,Smax-k)) % 10 );
            guests += max(k+1-S-guests,0);
        }
        out << guests;
        out << endl;
    }

    return 0;
}
