#include <iostream>
#include <fstream>

using namespace std;

string lastWord( string line )
{
    string res = "";
    res = res + line.at(0);
    for( size_t i = 1 ; i < line.length() ; i++ )
    {
        if( res.at(0) > line.at(i) )
        {
            res = res + line.at(i);
        }
        else
        {
            res = line.at(i) + res;
        }
    }
    return res;
}

int main()
{
    int numCases, cnt;
    string line;

    ifstream inf;
    ofstream outf( "A-large.out.txt" );
    inf.open( "A-large.in" );

    cnt = 0;
    inf >> numCases;
    inf.get(); // clear '\n'
    while( numCases-- )
    {
        getline( inf, line );

        outf << "Case #" << ++cnt << ": " << lastWord( line ) << endl;
    }

    inf.close();
    outf.close();
 
    return 0;
}
