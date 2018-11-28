#include <iostream>
#include <fstream>
#include <cstdlib>
#include <iomanip>

using namespace std;

void error( const char *str)
{
    cout << str;

    exit( 1);
}

int main()
{
    ifstream input( "input.txt");

    if ( !input )
        error( "Cannot open input file");

    ofstream output( "output.txt");

    if ( !output )
        error( "Cannot open output file");

    int num_cases;

    input >> num_cases;

    for ( int i = 0; i < num_cases; i++ )
    {
        double C = 0, F = 0, X = 0;

        input >> C >> F >> X;

        double result = 0, rate = 2;

        while ( X / rate > (C / rate) + (X / (rate + F)))
        {
            result += C / rate;
            rate += F;
        }

        result += X / rate;

        output << "Case #" << i + 1 << ": " << setiosflags(ios::fixed) << setprecision(7) << result << "\n";
    }

    return 0;
}
