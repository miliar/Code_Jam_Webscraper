#include <iostream>
#include <fstream>
#include <cstring>

int digits[ 10 ] = { 0 };

bool testNumber( unsigned long long val )
{
    // Discard trailing zeroes
    if ( val % 10 == 0 )
    {
        digits[ 0 ] = 1;
        do
        {
            val /= 10;
        }
        while ( val % 10 == 0 );
    }
    
    while ( val )
    {
        int dig = val % 10;
        val /= 10;
        digits[ dig ] = 1;
    }
    
    for ( int i = 0; i < 10; ++i )
    {
        if ( !digits[ i ] )
            return false;
    }
    
    return true;
}

int main( int argc, char** argv )
{
    std::ifstream fin( argv[ 1 ] );
    std::ofstream fout( "out1.txt" );
    
    int N;
    fin >> N;
    
    unsigned long long val;
    
    for ( int test = 1; test <= N; ++test )
    {
        memset( digits, 0, 10 * sizeof( int ) );
    
        fin >> val;
        fout << "Case #" << test << ": ";
        
        if ( !val )
        {
            fout << "INSOMNIA" << std::endl;
            continue;
        }
        
        int i = 1;
        while ( !testNumber( val * i ) )
            ++i;
        
        fout << val * i << std::endl;    
    }
}
