#include <iostream>
#include <map>
#include <set>
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
        
        map< int, int > m;
        
        int N;
        fin >> N;
        for ( int i = 0; i < 2 * N - 1; ++i )
        {
            for ( int j = 0; j < N; ++j )
            {
                int num;
                fin >> num;
                ++m[ num ];
            }
        }
        
        set< int > res;
        
        for ( auto it = m.begin(); it != m.end(); ++it )
        {
            if ( it->second % 2 )
            {
                res.insert( it->first );
            }
        }
        
        auto it2 = res.begin();
        set< int >::iterator it;
        for ( it = res.begin(); it != res.end(); ++it )
        {
            ++it2;
            if ( it2 == res.end())
                break;
            fout << *it << " ";
        }
        if ( res.size() )
            fout << *it;
        fout << endl;
    } 
    return 0;
}
