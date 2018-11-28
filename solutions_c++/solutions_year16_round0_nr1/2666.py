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
    //ifstream in("small-practice.in");
    ifstream in("A-large.in");
    ofstream out("output.out");

    int T;
    in >> T;

    for( int t = 1; t <= T; t++ )
    {
        out << "Case #" << t << ": ";

		long long n, number;
		in >> n;
		number = n;

		int digits[10] = {0,0,0,0,0,0,0,0,0,0};

		if( number == 0 )
		{
			out << "INSOMNIA";
		}
		else
		{
			do
			{
				long long div = 1;
				while( number/div != 0 )
				{
					digits[ (number/div)%10 ] = 1;
					div *= 10;
				}

				number += n;
			}
			while( find( begin(digits), end(digits), 0 ) != end(digits) );
			
			out << number-n;
		}

        out << endl;
    }

    return 0;
}
