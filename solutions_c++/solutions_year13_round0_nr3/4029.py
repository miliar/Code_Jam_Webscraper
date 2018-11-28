// I/O Includes

#include<new>
#include<cstdio>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<sstream>
#include<iostream>
#include<strstream>

// Data Structure Includes

#include<map>
#include<set>
#include<list>
#include<stack>
#include<deque>
#include<queue>
#include<vector>
#include<bitset>
#include<string>
#include<iterator>
#include<algorithm>

// Standard Namespace Inclusion

using namespace std;

// Supporting Macros

#define SZ( C )                 ( ( int ) ( ( C ).size() ) )
#define ALL( C )                ( C ).begin() , ( C ).end()
#define TR( C , it )            for( typeof( ( C ).begin() ) it = ( C ).begin(); it != ( C ).end() ; ++it )
#define LN( STRING )            ( ( int ) ( STRING ).length() )
#define SPRESENT( C , x )       ( ( ( C ).find( x ) ) != ( C ).end() )
#define CPRESENT( C , x )       ( find( ALL( C ) , x ) != ( C ).end() )
#define PB                      push_back

// Typedefed Versions of Data Types

typedef vector< int > VI;
typedef vector< VI > VVI;
typedef vector< string > VS;
typedef pair< int ,int > PII;
typedef long long LL;
typedef unsigned long long ULL;

int main(){

    vector< ULL > fairAndSquare;

    fairAndSquare.PB( 1 );
    fairAndSquare.PB( 4 );
    fairAndSquare.PB( 9 );
    fairAndSquare.PB( 121 );
    fairAndSquare.PB( 484 );
    fairAndSquare.PB( 10201 );
    fairAndSquare.PB( 12321 );
    fairAndSquare.PB( 14641 );
    fairAndSquare.PB( 40804 );
    fairAndSquare.PB( 44944 );
    fairAndSquare.PB( 1002001 );
    fairAndSquare.PB( 1234321 );
    fairAndSquare.PB( 4008004 );
    fairAndSquare.PB( 100020001 );
    fairAndSquare.PB( 102030201 );
    fairAndSquare.PB( 104060401 );
    fairAndSquare.PB( 121242121 );
    fairAndSquare.PB( 123454321 );
    fairAndSquare.PB( 125686521 );
    fairAndSquare.PB( 400080004 );
    fairAndSquare.PB( 404090404 );
    fairAndSquare.PB( 10000200001 );
    fairAndSquare.PB( 10221412201 );
    fairAndSquare.PB( 12102420121 );
    fairAndSquare.PB( 12345654321 );
    fairAndSquare.PB( 40000800004 );
    fairAndSquare.PB( 1000002000001 );
    fairAndSquare.PB( 1002003002001 );
    fairAndSquare.PB( 1004006004001 );
    fairAndSquare.PB( 1020304030201 );
    fairAndSquare.PB( 1022325232201 );
    fairAndSquare.PB( 1024348434201 );
    fairAndSquare.PB( 1210024200121 );
    fairAndSquare.PB( 1212225222121 );
    fairAndSquare.PB( 1214428244121 );
    fairAndSquare.PB( 1232346432321 );
    fairAndSquare.PB( 1234567654321 );
    fairAndSquare.PB( 4000008000004 );
    fairAndSquare.PB( 4004009004004 );
    fairAndSquare.PB( 100000020000001 );


    freopen("/home/ankit/Desktop/C-large-1.in" , "rb" , stdin);
    freopen("/home/ankit/Desktop/C-large-1.out" , "wb" , stdout);

    int T;
    cin >> T;

    int test = 0;

    while( T-- ){

        ++test;

        ULL A , B;
        cin >> A >> B;

        int no = 0;

        for(int i = 0 ; i < SZ( fairAndSquare ) ; ++i){

            if( fairAndSquare[i] >= A && fairAndSquare[i] <= B )
                ++no;
        }

        cout <<"Case #" << test <<": " << no << endl;
    }

    getchar();
    getchar();

    return 0;
}
