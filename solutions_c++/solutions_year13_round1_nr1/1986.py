#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

typedef struct {
    //Data
    double r, t;
} CaseData;

const double pi = 3.141592653589;

std::string solve( CaseData data ){
    //Code
    std::stringstream result;
    double r = data.r;
    
    double count = 0;

    double volRec = 0;
    while( volRec <= data.t ){
        count++;
        volRec = count * ( 2*r + 2*count - 1 );
        std::cout << "count: " << count << "t: " << data.t << " v: " << volRec << std::endl;
    }


    result << " " << --count;

    return result.str();
}

int main(int argc, const char *argv[])
{
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
        //Blah
        //
        
        infile >> data.r;
        infile >> data.t;

        outfile << "Case #" << i << ":" << solve( data ) << std::endl;
    }


    return 0;
}
