#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath>
using namespace std;

bool isPalindrome( int n );
int FindFairSquaresBetween( int start, int end );

// WARNING!  We may be asked to count to a googol (10^100)...
// How the hell is that going to work?
// Do I have (or build) 333-bit integers?
int main( int argc, char* argv[] ) {
    ifstream infile( "small.txt" );
    int num_cases;
    int start_interval;
    int end_interval;

    infile >> num_cases;
    for ( int i = 0; i < num_cases; i++ ) {
        infile >> start_interval;
        infile >> end_interval; 
       
        cout << "Case #" << ( i + 1 ) << ": " << FindFairSquaresBetween( start_interval, end_interval ) << endl; 
    }

    return 0;
}

int FindFairSquaresBetween( int start, int end ) {
    int num_fair_squares = 0;
   
    // How can I tell if a number is a square? Is it safe to test the fractional portion after a call to sqrtf()? 
    for ( int i = start; i <= end; i++ ) {
        float square_root;
        bool isSquareRootIntegral = false;

        square_root = sqrtf( i );
        isSquareRootIntegral = ( square_root - ( (int) square_root ) == 0.0f );
        if ( isPalindrome( i ) && isSquareRootIntegral && isPalindrome( square_root )  )
            num_fair_squares++;
    }

    return num_fair_squares;
}

// Can I do this without strings?
bool isPalindrome( int n ) {
    stringstream ss;
    string n_str;
    string rev_n_str;

    ss << n;
    n_str = ss.str();
    rev_n_str = ss.str();
    reverse( rev_n_str.begin(), rev_n_str.end() );

    return ( n_str == rev_n_str ); 
}
