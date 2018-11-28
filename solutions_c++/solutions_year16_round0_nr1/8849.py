#include <iostream>
#include <fstream>

using namespace std;                                    

bool isDone( bool d[] )
{
    return d[0] && d[1] && d[2] && d[3] && d[4] && d[5] && d[6] && d[7] && d[8] && d[9];
}

void update( long N, bool digits[] )
{
    while( N )
    {
        digits[N%10] = true;
        N /= 10;
    }
}

string test( long N )
{
    bool digits[10] = { 0 };
    long mult = 1;
    update( N, digits );
    if( N == 0 )
    {
        return "INSOMNIA";
    }
    else
    {
        while( !isDone( digits ) )
        {
            mult++;
            //cout << N << endl;
            update( N*mult, digits );
        }
        //cout << N << endl;
        return to_string(N*mult);
    }
}

int main()
{   
    // TEST for all N --> DOES HALT FOR ALL
    /*
    for( long i = 0 ; i < 1000001 ; i++ )
    {
        cout << "N: " << i << "\t" << test( i ) << endl;
    }*/

    int numCases;
    long N;

    ifstream infile;
    ofstream outfile( "A-large.out" );
    infile.open( "A-large.in" );

    infile >> numCases;
    int cnt = 0;
    while( numCases-- )
    {
        infile >> N;
        outfile << "CASE #" << ++cnt << ": " << test( N ) << endl;
    }
    infile.close();
    outfile.close();
}
