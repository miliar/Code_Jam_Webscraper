#include <iostream>
#include<string.h>
#include<stack>
#include<stdio.h>
#include <stdlib.h>
#include <sstream>
#include <time.h>
#include <vector>
using namespace std;
unsigned long long str2int( string s )
{
    unsigned long long res;
    sscanf( s.c_str(), "%I64u", &res );
    return res;
}
int casid;
int main()
{
    int cas;
    string s;
    freopen( "A-small-attempt1.in", "r", stdin );
    freopen( "A-small-attempt1.out", "w", stdout );
    cin >> cas;
    while ( cas-- )
    {
        cin >> s;
        int ans = -1;
        unsigned long long p = str2int( s.substr( 0, s.find_first_of( "/" ) ) ), q = str2int( s.substr( s.find_first_of( "/" ) + 1 ) );
        for ( int i = 0; i < 40 && q > 1; i++ )
        {
            if ( (q % 2) == 0 )
            q /= 2;
            else
            {
                ans = -1;
                break;
            }
            if ( p >= q && ans == -1 )
            {
                ans = i + 1;
                //break;
            }
        }
        if ( q != 1 && (q % 2) != 0 )
        ans = -1;
        cout << "Case #"<< ++casid <<": ";
        if ( ans == -1 )
        {
            cout << "impossible" << endl;
        }
        else
        {
            cout << ans << endl;
        }
    }

	return 0;
}

