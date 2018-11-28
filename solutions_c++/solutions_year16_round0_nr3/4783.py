#include <fstream>
#include <iostream>
#include <bitset>
#include <cmath>

#define NUM_SIZE 16ULL

using namespace std;

bool isPrime( unsigned long long num, unsigned long long* firstDiv )
{
    unsigned long long upperLimit = sqrt( num );
    
    *firstDiv = 0;
    
    for ( unsigned long long i = 3; i < upperLimit; ++i )
    {
        if ( num % i == 0 )
        {
            *firstDiv = i;
            return false;
        }
    }
    
    return true;
}

unsigned long long getInBase( unsigned long long num, int base )
{
    if ( base == 2 )
        return num;
    base -= 3;
    
    static unsigned long long bases[ 8 ][ 16 ] = {
        { 1ULL, 3ULL, 9ULL, 27ULL, 81ULL, 243ULL, 729ULL, 2187ULL, 6561ULL, 19683ULL, 59049ULL, 177147ULL, 531441ULL, 1594323ULL, 4782969ULL, 14348907ULL },
        { 1ULL, 4ULL, 16ULL, 64ULL, 256ULL, 1024ULL, 4096ULL, 16384ULL, 65536ULL, 262144ULL, 1048576ULL, 4194304ULL, 16777216ULL, 67108864ULL, 268435456ULL, 1073741824ULL },
        { 1ULL, 5ULL, 25ULL, 125ULL, 625ULL, 3125ULL, 15625ULL, 78125ULL, 390625ULL, 1953125ULL, 9765625ULL, 48828125ULL, 244140625ULL, 1220703125ULL, 6103515625ULL, 30517578125ULL },
        { 1ULL, 6ULL, 36ULL, 216ULL, 1296ULL, 7776ULL, 46656ULL, 279936ULL, 1679616ULL, 10077696ULL, 60466176ULL, 362797056ULL, 2176782336ULL, 13060694016ULL, 78364164096ULL, 470184984576ULL },
        { 1ULL, 7ULL, 49ULL, 343ULL, 2401ULL, 16807ULL, 117649ULL, 823543ULL, 5764801ULL, 40353607ULL, 282475249ULL, 1977326743ULL, 13841287201ULL, 96889010407ULL, 678223072849ULL, 4747561509943ULL },
        { 1ULL, 8ULL, 64ULL, 512ULL, 4096ULL, 32768ULL, 262144ULL, 2097152ULL, 16777216ULL, 134217728ULL, 1073741824ULL, 8589934592ULL, 68719476736ULL, 549755813888ULL, 4398046511104ULL, 35184372088832ULL },
        { 1ULL, 9ULL, 81ULL, 729ULL, 6561ULL, 59049ULL, 531441ULL, 4782969ULL, 43046721ULL, 387420489ULL, 3486784401ULL, 31381059609ULL, 282429536481ULL, 2541865828329ULL, 22876792454961ULL, 205891132094649ULL },
        { 1ULL, 10ULL, 100ULL, 1000ULL, 10000ULL, 100000ULL, 1000000ULL, 10000000ULL, 100000000ULL, 1000000000ULL, 10000000000ULL, 100000000000ULL, 1000000000000ULL, 10000000000000ULL, 100000000000000ULL, 1000000000000000ULL }
    };
    
    unsigned long long result = 0;
    int index = 0;
    while ( num )
    {
        if ( num & 1 )
            result += bases[ base ][ index ];
        ++index;
        num >>= 1;
    }
    return result;
} 

int main( int argc, char** argv )
{
    ofstream fout( "out1.txt" );
    
    const unsigned long long upperLimit =  (1ULL << NUM_SIZE );
    int counter = 0;
    fout << "Case #1:" << endl;
    for ( unsigned long long i = ( 1ULL << ( NUM_SIZE - 1ULL ) ) + 1ULL; i < upperLimit && counter < 50; i += 2 )
    {
        bool checkOdd = true;
        if ( __builtin_popcountll( i ) % 2 == 0 )
        {
            checkOdd = false;
        }
        
        unsigned long long divisors[ 9 ] = { 0ULL };
        bool isGood = true;
        for ( int base = 2; base <= 10; ++base )
        {
            if ( !checkOdd && base % 2 == 1 )
            {
                divisors[ base - 2 ] = 2;
                continue;
            }
            if ( isPrime( getInBase( i, base ), &divisors[ base - 2 ] ) )
            {
                isGood = false;
                break;
            }
        }
        
        if ( isGood )
        {
            fout << bitset< NUM_SIZE >( i ) << " ";
            for ( int j = 0; j < 8; ++j )
            {
                fout << divisors[ j ] << " ";
            }
            fout << divisors[ 8 ] << endl;
            ++counter;
        }
    }
    
    return 0;
}

