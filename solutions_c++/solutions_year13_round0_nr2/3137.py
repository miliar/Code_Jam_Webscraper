#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

typedef struct {
    //Data
    int row, col;
    std::vector<int> height;

    std::vector<int> getRow( int r ) const{
        std::vector<int> thisRow;
        //std::cout << "Row " << r << ": ";
        for( int i = 0; i < col; i++ ){
            thisRow.push_back( height[ (r-1) * col + i] );
            //std::cout << thisRow[i];
        }
        //std::cout << std::endl;
        return thisRow;
    }

    std::vector<int> getCol( int c ) const{
        std::vector<int> thisCol;
        //std::cout << "Col " << c << ": ";
        for( int i = 0; i < row; i++ ){
            thisCol.push_back( height[ i * col + ( c-1) ] );
            //std::cout << thisCol[i];
        }
        //std::cout << std::endl;
        return thisCol;
    }
} CaseData;

int findMax( const std::vector<int> &v ){
    int max = 0;
    for( int i = 0; i < v.size(); i ++ )
        if( v[i] > max ) max = v[i];
    return max;
}

int findMin( const std::vector<int> &v ){
    int min = 101;
    for( int i = 0; i < v.size(); i ++ )
        if( v[i] < min ) min = v[i];
    return min;
}

bool isReachable( const CaseData &d, int row, int col ){
    int idx = (row-1) * d.col + (col - 1);
    bool reachableR = true;
    bool reachableC = true;
    int thisSquare = d.height[idx];
    //std::cout << "at: " << row << ", " << col <<  " (" << thisSquare << ")" << std::endl;
    //has squares taller in row?
    if( thisSquare < findMax( d.getRow( row ) ) ){
        //std::cout << "Not max in row" << std::endl;
        reachableR = false;
    }
    //now colmn
    if( thisSquare < findMax( d.getCol( col ) ) ){
        //std::cout << "Not max in col" << std::endl;
        reachableC = false;
    }

    return reachableR || reachableC;
}

std::string solve( CaseData data ){
    for( int r = 1; r <= data.row; r++ )
        for( int c = 1; c <= data.col; c++ )
            if( !isReachable( data, r, c ) )
                return "NO";
    return "YES";

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
        infile >> data.row;
        infile >> data.col;
        for( int j = 0; j < (data.row * data.col); j++){
            int height;
            infile >> height;
            data.height.push_back(height);
        }

        outfile << "Case #" << i << ": " << solve( data ) << std::endl;
    }


    return 0;
}
