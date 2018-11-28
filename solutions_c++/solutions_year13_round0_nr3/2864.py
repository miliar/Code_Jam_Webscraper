#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <cmath>
#include <boost/math/special_functions.hpp>

typedef struct {
    //Data
    int start; int end;
} CaseData;

bool isSquare( int i ){
    int root( boost::math::round (std::sqrt( (double) i ) ) );
    return i == root * root;
}

bool isFair( int i ){
    std::stringstream inputNum;
    inputNum << i;
    int strLen = inputNum.str().length();
    bool fair = true;
    for( int i = 0; i < (strLen/2); i++){
        if( inputNum.str()[i] != inputNum.str()[strLen-1-i] ){
            fair = false;
            break;
        }

    }
 
    return fair;
}

std::string solve( CaseData data ){
    //Code
    std::stringstream result;
    int count = 0;
    for( int i = data.start; i <= data.end; i++){
        int s_i = boost::math::round(std::sqrt(i));
        if( isSquare(i) && isFair(i) )
            if( isFair( s_i ) )
                count++;
    }

    result << count;

    return result.str();
}

int main(int argc, const char *argv[])
{
    //std::cout << "test isSquare: " << isSquare(4) << std::endl;
    //std::cout << "test isFair(12321): " << isFair( 4 ) << std::endl;

    if( argc != 3 ){
        std::cerr << "argument error" << std::endl;
        return -1;
    }

    std::ifstream infile( argv[1] );
    std::ofstream outfile( argv[2] );

    std::cerr << argv[1] << " -> " << argv[2] << std::endl;
   

    //Read Cases
    int numCases;
    if( infile.is_open() ){
        infile >> numCases;
    } else {
        std::cerr << "Failed to open input" << std::endl;
        return -1;
    }

    std::string garbage;
    std::getline( infile, garbage );

    for( int i = 1; i <= numCases; i++ ){
        CaseData data;
        //Populate data
        infile >> data.start;
        infile >> data.end;
        //std::cout << data.start << " to " << data.end << std::endl;
        outfile << "Case #" << i << ": " << solve( data ) << std::endl;
    }


    return 0;
}
