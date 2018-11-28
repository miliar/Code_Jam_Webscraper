#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main( int argc, char** argv )
{
    ifstream fin( argv[ 1 ] );
    ofstream fout( "out.txt" );
    
    int N;
    fin >> N;
    while ( fin.get() != '\n' );
    
    for ( int test = 1; test <= N; ++test )
    {
        fout << "Case #" << test << ": ";
        
        string input;
        getline( fin, input );
        
        if ( !input.size() )
        {
            fout << 0 << endl;
            continue;
        }
        
        input.insert( input.end(), '+' );
        
        int cnt = 0;
        for ( string::iterator it = input.begin() + 1; it != input.end(); ++it )
        {
            if ( *( it - 1 ) != *it )
            {
                ++cnt;
            }
        }
        fout << cnt << endl;
    }
    
    return 0;
}

