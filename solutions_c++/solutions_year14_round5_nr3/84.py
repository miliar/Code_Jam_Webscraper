#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <algorithm>
#include <iomanip>
#include <queue>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <stack>
#include <bitset>
#include <sstream>
#include <fstream>

typedef unsigned long long ull;
#define mp make_pair
#define pb push_back

const long double eps = 1e-9;
const double pi = acos(-1.0);
const long long inf = 1e18;

using namespace std;

int n, h, mapping[ 2222 ];
pair< string, int > actions[ 20 ];
bool f[ 16 ][ 32768 ];

void solve()
{
    cin >> n;
    h = 0;
    memset( mapping, 0, sizeof( mapping ) );
    for ( int i = 0; i < n; i++ )
    {
        cin >> actions[i].first >> actions[i].second;
        if ( actions[i].second != 0 )
        {
            int id = actions[i].second;
            if ( mapping[ id ] == 0 )
            {
                h += 1;
                mapping[ id ] = h;
            } 
            actions[i].second = mapping[ id ];
        }
        //cout << actions[i].first << " " << actions[i].second << "\n";
    }
    memset( f, false, sizeof( f ) );
    for ( int i = 0; i < 32768; i++ ) f[0][i] = true;
    for ( int i = 0; i < n; i++ )
    {
        char c = actions[i].first[0];
        int person = actions[i].second;
        for ( int msk = 0; msk < 32768; msk++ )
        {
            if ( f[i][msk] == false ) continue;
            if ( c == 'L' && person != 0 )
            {
                int bit = ( 1 << ( person - 1 ) );
                if ( ( msk & bit ) != 0 )
                {
                    f[i + 1][ msk ^ bit ] = true;
                } 
            }
            if ( c == 'E' && person != 0 )
            {
                int bit = ( 1 << ( person - 1 ) );
                if ( ( msk & bit ) == 0 )
                {
                    f[i + 1][ msk ^ bit ] = true;
                } 
            }
            if ( c == 'L' && person == 0 )
            {
                for ( int person = 1; person <= 15; person++ )
                {
                    int bit = ( 1 << ( person - 1 ) );
                    if ( ( msk & bit ) != 0 )
                    {
                        f[i + 1][ msk ^ bit ] = true;
                    } 
                }
            }
            if ( c == 'E' && person == 0 )
            {
                for ( int person = 1; person <= 15; person++ )
                {
                    int bit = ( 1 << ( person - 1 ) );
                    if ( ( msk & bit ) == 0 )
                    {
                        f[i + 1][ msk ^ bit ] = true;
                    } 
                }
            }
        }
    }
    int answer = 1000;
    for ( int i = 0; i < 32768; i++ ) if ( f[n][i] ) answer = min( answer, __builtin_popcount( i ) );
    if ( answer == 1000 ) cout << "CRIME TIME"; else cout << answer;  
}

int main (int argc, const char * argv[])
{
    int testcase; scanf("%d", &testcase);
    for ( int test = 1; test <= testcase; test++ ) 
    {
        printf("Case #%d: ", test);
        solve();
        printf("\n");
    }
    return 0;
}