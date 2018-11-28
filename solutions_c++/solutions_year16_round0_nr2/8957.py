#include <iostream>
#include <fstream>
                 
using namespace std;

bool toFlip( char symbol, bool isFlipped )
{
    if( isFlipped ) 
    {
        if( symbol == '+' )
        {
            return true;
        }
        else
            return false;
    }
    else
    {
        if( symbol == '-' )
        {
            return true;
        }
        else
            return false;
    }
}

int test( string line )
{
    bool isFlipped = false;
    int number_of_flips = 0;
    for( int i = (int)line.length()-1 ; i >= 0 ; i-- )
    {
        if( toFlip( line.at(i), isFlipped ) )
        {
            isFlipped = !isFlipped;
            number_of_flips++;
        }
    } 
    return number_of_flips;
}

int main()
{
    int numCases, cnt;
    string line;

    ifstream inf;
    ofstream outf( "B-large.out" );
    inf.open( "B-large.in" );

    inf >> numCases;
    inf.get(); // clear '\n'
                      
    cnt = 0;
    while( numCases-- )
    {
        getline( inf, line );
        outf << "Case #" << ++cnt << ": " << test( line ) << endl;
    }
    outf.close();
    inf.close();

    return 0;
}
