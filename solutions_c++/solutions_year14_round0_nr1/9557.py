/**
 * @file magicTrick.cpp
 * @brief Guess the letter
 */
#include <iomanip>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <math.h>
#include <vector>

/**
 * @function main
 */
int main( int argc, char* argv[] ) {

  if( argc != 2 ) {
    std::cout << "Syntax: "<<argv[0]<<" "<<argv[1]<<std::endl;
    return -1;
  }

  std::ifstream input;
  std::ofstream output;
  std::string line;
  int T; // Number of test cases
  int row1, row2; // Velocity and horizontal distance
  int cards1[4][4];
  int cards2[4][4];
  double theta;

  input.open( argv[1], std::ios::in );
  output.open( "magicTrickResult.txt", std::ios::out );

  if( input.is_open() ) {
    std::getline( input, line );
    std::stringstream( line ) >> T;
    
    for( int i = 0; i < T; i++ ) {
      std::cout << "Test case: "<< i+1 << std::endl;

      // Read answer row 1
      std::getline( input, line );
      std::stringstream( line ) >> row1;
      // Read card order 1
      std::getline( input, line );
      std::stringstream( line ) >> 
	cards1[0][0] >> cards1[0][1] >> cards1[0][2] >> cards1[0][3];
      std::getline( input, line );
      std::stringstream( line ) >> 
	cards1[1][0] >> cards1[1][1] >> cards1[1][2] >> cards1[1][3];
      std::getline( input, line );
      std::stringstream( line ) >> 
	cards1[2][0] >> cards1[2][1] >> cards1[2][2] >> cards1[2][3];
      std::getline( input, line );
      std::stringstream( line ) >> 
	cards1[3][0] >> cards1[3][1] >> cards1[3][2] >> cards1[3][3];

      // Read answer row 2
      std::getline( input, line );
      std::stringstream( line ) >> row2;
      // Read card order 2
      std::getline( input, line );
      std::stringstream( line ) >> 
	cards2[0][0] >> cards2[0][1] >> cards2[0][2] >> cards2[0][3];
      std::getline( input, line );
      std::stringstream( line ) >> 
	cards2[1][0] >> cards2[1][1] >> cards2[1][2] >> cards2[1][3];
      std::getline( input, line );
      std::stringstream( line ) >> 
	cards2[2][0] >> cards2[2][1] >> cards2[2][2] >> cards2[2][3];
      std::getline( input, line );
      std::stringstream( line ) >> 
	cards2[3][0] >> cards2[3][1] >> cards2[3][2] >> cards2[3][3];


      std::cout << "Row 1: "<< row1 << std::endl;
      std::cout << "Matrix: "<< std::endl;
      for( int a = 0; a < 4; a++ ) {
	for( int b = 0; b < 4; ++b ) {
	  std::cout << cards1[a][b] << " ";
	} std::cout << std::endl;
      }


      std::cout << "Row 2: "<< row2 << std::endl;
      std::cout << "Matrix: "<< std::endl;
      for( int a = 0; a < 4; a++ ) {
	for( int b = 0; b < 4; ++b ) {
	  std::cout << cards2[a][b] << " ";
	} std::cout << std::endl;
      }

      // Compare the row elements and see how many coincidences you get
      std::vector<int> answers;
      for( int j= 0; j < 4; ++j ) {
	for( int k = 0; k < 4; ++k ) {
	  if( cards1[row1-1][j] == cards2[row2-1][k] ) {
	    answers.push_back( cards1[row1-1][j] );
	    break;
	  }
	}
      }
      
      if( answers.size() == 1 ) {
	output << "Case #"<<i+1<<": "<<answers[0]<<std::endl;
      } else if( answers.size() == 0 ) {
	output << "Case #"<<i+1<<": "<<"Volunteer cheated!"<<std::endl;      
      } else if( answers.size() > 1 ) {
	output << "Case #"<<i+1<<": "<<"Bad magician!"<<std::endl;            
      }


    }

  } else {
    std::cout << "[X] Error opening input file"<< std::endl;
  }

  output.close();
  input.close();

  return 0;
}

