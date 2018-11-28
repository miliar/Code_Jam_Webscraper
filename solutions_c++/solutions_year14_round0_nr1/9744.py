#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

int main( int argc, const char* argv[] ) {

  std::string line;
  std::ifstream jam_file( argv[1] );
  int test_count, test_i, board_i;
  
  jam_file >> test_count;
  
  for( test_i = 0; test_i < test_count; test_i++ ){
  
    int j, k, r1, r2, board1[4][4], board2[4][4];
    std::vector<int> pos;
    
    jam_file >> r1;
    r1--;
    
    for( board_i = 0; board_i < 4; board_i++ ) {
      jam_file >> board1[board_i][0] >> board1[board_i][1] >> board1[board_i][2] >> board1[board_i][3];
    }
    
    jam_file >> r2;
    r2--;
    
    for( board_i = 0; board_i < 4; board_i++ ) {
      jam_file >> board2[board_i][0] >> board2[board_i][1] >> board2[board_i][2] >> board2[board_i][3];
    }
    
    for( j = 0; j < 4; j++ ) {
      for( k = 0; k < 4; k++ ) {
        if(board1[r1][j] == board2[r2][k]) {
          pos.push_back(board1[r1][j]);
        }
      }
    }
   
    std::cout << std::endl;
    
    std::cout << "Case #" << test_i + 1 << ": ";
    
    if( pos.size() == 0 ) {
      std::cout << "Volunteer cheated!";
    } else if( pos.size() == 1 ) {
      std::cout << pos[0];
    } else {
      std::cout << "Bad magician!";
    }
    
  }
  
  std::cout << std::endl;
  
  jam_file.close();

  return 0;

}