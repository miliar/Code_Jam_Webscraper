#include <iostream>
#include <fstream>
#include <cstring>
#include <sstream>
#include <cmath>

bool pal ( int n ) {

    int i;

    std::string pal;
    std::stringstream convert;
    convert << n;
    pal = convert.str();

    for ( i = 0 ; i < ( ( pal.length() / 2 ) + 0.5 ) ; ++i ) {

        if ( pal[i] != pal[pal.length()-1-i] )
            return false;
    }

    return true;
}

int FandS ( int A , int B ) {

    int i;

    int n ( 0 );

    for ( i = ( sqrt ( A ) ) ; i*i <= B ; ++i ) {

        if ( ( pal ( i ) ) && ( ( i * i ) >= A ) && ( pal ( i * i ) ) )
            n++;
    }

    return n;
}

int main ( int argc , char *argv[] ) {

    std::ifstream input ( "input.txt" );
    std::ofstream output ( "output.txt" );
    if ( !input ) std::cout << "failed to open file." << std::endl;
    else {

        int i , n , A , B;

        input >> n;

        for ( i = 0 ; i < n ; ++i ) {

            input >> A >> B;

            output << "Case #" << i+1 << ": ";
            output << FandS ( A , B );
            output << std::endl;
        }
    }

    return 0;
}
