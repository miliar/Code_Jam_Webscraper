#include <fstream>
#include <iostream>
#include <set>
#include <functional>

using namespace std;

int main( int argc, char** argv )
{
    ifstream fin( argv[ 1 ] );
    ofstream fout( "out1.txt" );
    
    int T;
    fin >> T;
    
    for ( int test = 1; test <= T; ++test )
    {
        fout << "Case #" << test << ":";
        
        std::string result;
        
        int N;
        fin >> N;
        multiset< std::pair< int, int >, std::greater< std::pair< int, int > > > p;
        int tmp;
        for ( int i = 0; i < N; ++i )
        {
            fin >> tmp;
            p.insert( std::make_pair( tmp, i ) );
        }
        
        while ( p.size() > 0 )
        {
            auto it = p.begin();
            ++it;
            if ( ( p.size() == 2 && p.begin()->first != ( it )->first ) || p.size() != 2 )
            {
                std::pair< int, int > cur_val = *p.begin();
                p.erase( p.begin() );
                --cur_val.first;
                if ( cur_val.first )
                    p.insert( cur_val );
                result += " ";
                result += char( cur_val.second + 'A' );
            }
            else if ( p.size() == 2 )
            {
                result += " ";
                result += char( p.begin()->second + 'A' );
                std::pair< int, int > cur_val = *p.begin();
                --cur_val.first;
                p.erase( p.begin() );
                if ( cur_val.first )
                    p.insert( cur_val );
                result += char( p.begin()->second + 'A' );
                cur_val = *p.begin();
                --cur_val.first;
                p.erase( p.begin() );
                if ( cur_val.first )
                    p.insert( cur_val );
            }
            else
            {
                result += " ";
                result += char( p.begin()->second + 'A' );
                p.erase( p.begin() );
            }
            //cout << result << endl;
        }
        
        fout << result;
        
        fout << endl;
    }
    
    return 0;
}

