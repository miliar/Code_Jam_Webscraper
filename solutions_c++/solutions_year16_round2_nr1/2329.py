#include <fstream>
#include <iostream>
#include <set>
#include <map>

using namespace std;

int main( int argc, char** argv )
{
    ifstream fin( argv[ 1 ] );
    ofstream fout( "out.txt" );
    
    int T;
    fin >> T;
    
    fin.ignore( 100, '\n' );
    
    for ( int testCase = 1; testCase <= T; ++testCase )
    {
        fout << "Case #" << testCase << ": ";
        
        map< char, int > freq;
        
        char c;
        while ( fin.get( c ) && c != '\n' && c != '\r' )
        {
            ++freq[ c ];
        }
        
        multiset< int > res;
        
        // Get all zeros
        while ( freq[ 'Z' ] )
        {
            --freq[ 'Z' ];
            --freq[ 'E' ];
            --freq[ 'R' ];
            --freq[ 'O' ];
            res.insert( 0 );
        }
        
        // Get all sixes
        while ( freq[ 'X' ] )
        {
            --freq[ 'S' ];
            --freq[ 'I' ];
            --freq[ 'X' ];
            res.insert( 6 );
        }
        
        // Get all eights
        while ( freq[ 'G' ] )
        {
            --freq[ 'E' ];
            --freq[ 'I' ];
            --freq[ 'G' ];
            --freq[ 'H' ];
            --freq[ 'T' ];
            res.insert( 8 );
        }
        
        // Get all threes
        while ( freq[ 'H' ] )
        {
            --freq[ 'T' ];
            --freq[ 'H' ];
            --freq[ 'R' ];
            --freq[ 'E' ];
            --freq[ 'E' ];
            res.insert( 3 );
        }
        
        // Get all twos
        while ( freq[ 'T' ] )
        {
            --freq[ 'T' ];
            --freq[ 'W' ];
            --freq[ 'O' ];
            res.insert( 2 );
        }
        
        // Get all fours
        while ( freq[ 'U' ] )
        {
            --freq[ 'F' ];
            --freq[ 'O' ];
            --freq[ 'U' ];
            --freq[ 'R' ];
            res.insert( 4 );
        }
        
        // Get all ones
        while ( freq[ 'O' ] )
        {
            --freq[ 'O' ];
            --freq[ 'N' ];
            --freq[ 'E' ];
            res.insert( 1 );
        }
        
        // Get all fives
        while ( freq[ 'F' ] )
        {
            --freq[ 'F' ];
            --freq[ 'I' ];
            --freq[ 'V' ];
            --freq[ 'E' ];
            res.insert( 5 );
        }
        
        // Get all sevens
        while ( freq[ 'S' ] )
        {
            --freq[ 'S' ];
            --freq[ 'E' ];
            --freq[ 'V' ];
            --freq[ 'E' ];
            --freq[ 'N' ];
            res.insert( 7 );
        }
        
        // nines
        while ( freq[ 'N' ] )
        {
            --freq[ 'N' ];
            --freq[ 'I' ];
            --freq[ 'N' ];
            --freq[ 'E' ];
            res.insert( 9 );
        }
        
        for ( auto i = res.begin(); i != res.end(); ++i )
        {
            fout << *i;
        }
        fout << endl;
    }
}

