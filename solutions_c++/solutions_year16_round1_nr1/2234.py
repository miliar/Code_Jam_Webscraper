#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main(int argc, char** argv)
{
    ifstream fin( argv[1] );
    ofstream fout("out.txt");
    
    int tests;
    fin >> tests;
    fin.ignore( 10, '\n' );
    for (int test = 1; test <= tests; ++test)
    {
        fout << "Case #" << test << ": ";
        
        string s;
        getline( fin, s );
        string res;
        res.push_back( s[ 0 ] );
        
        for ( auto i = s.begin() + 1; i != s.end(); ++i )
        {
            if ( *i >= res[ 0 ] )
            {
                res.insert( 0, 1, *i );
            }
            else
            {
                res.push_back(*i);
            }
        }
        
        fout << res << endl;
    } 
    return 0;
}
