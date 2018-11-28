#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>

using namespace std;

bool is_palindrome ( int x )
{
    int y = 0, z = x;

    do
        y = y * 10 + x % 10;
    while ( x /= 10 );

    return z == y ? true : false; 
}

bool is_squared( double x) 
{
    return ( ((int)(sqrt(x)))*((int)(sqrt(x))) == x );
}

int main(int argc, char* argv[] )
{
    ifstream infile ( argv[1] );
    ofstream outfile ( "output.txt" );

    if( infile.is_open() )
    {


        string line;
        getline( infile, line );

        int testcases = 0, testnumber = 0;

        stringstream ss;
        ss << line << endl;
        ss >> testcases;

        while (testcases)
        {
            testcases--;
            testnumber++;
            getline( infile, line );
            ss.str("");
            ss.clear();

            int i, j, count = 0;
            
            ss << line;
            ss >> i;
            ss >> j;

            for( i = i; i < j + 1; i++)
            {
                if( is_palindrome( i ) )
                    if ( is_squared ( i ) )
                        if ( is_palindrome ( sqrt ( (double) i ) ) ) 
                        {
                        cout << i << endl;
                        count++;
                        }
            }
            
            outfile << "Case #" << testnumber << ": " << count << endl;
        }

    }

    infile.close();
    outfile.close();
    return 0;
}
    
