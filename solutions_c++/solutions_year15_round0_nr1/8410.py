

#include <iostream>
#include <fstream>
#include <algorithm>

#define dim 1009
using namespace std;
ofstream out("stov.out");


int main()
{
    ifstream in("stov.in");

    int T;

    in >> T;
    for( int j = 1 ; j <= T;  ++j)
    {

        int Smax ;
        int nrpers = 0 , nr_priet = 0;
        char sir[dim] ;
        in >> Smax >> sir;
        nrpers = sir[0] - '0';

        for( int i = 1 ; sir[i] ; i++)
        {
                if( nrpers >= i )
            {
                nrpers+=sir[i] - '0';
            }
            else
            {
                ++nr_priet;
                ++nrpers;
                nrpers+=sir[i] - '0';
            }

        }

        out << "Case #" << j <<": " << nr_priet << "\n";
    }

    return 0;
}
