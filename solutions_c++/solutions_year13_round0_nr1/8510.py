#include <iostream>
#include <string>
#include <fstream>
#include <sstream>

int X = 1;
int O = 3;
int T = 2;
int DOT = 0;

enum Result {
  X_WON = 0,
  O_WON,
  DRAW,
  NOT_COMPLETED
};


Result calc(int board[]);
void printBoard(int board[]);


int main(int argc, char** argv) {
  
  if(argc == 0) {
    std::cout << "input file name." << std::endl;
    return -1;
  }
  
  std::string filename( argv[1] );
  std::ifstream ifs( filename.c_str() );
  std::string buf;

  std::ofstream ofs("Output.txt");

  int test_case_size;

  ifs >> buf;
  std::istringstream is( buf );
  is >> test_case_size;

  for( int i = 0; i < test_case_size; i++ ) {
    int board[16];

    //read
    for( int j = 0; j < 4; j++ ) {
      ifs >> buf;
      for( int k = 0; k < 4; k++ ) {
	switch( buf[k] ) {
	case 'X':
	  board[k+j*4] = X;
	  break;
	case 'O':
	  board[k+j*4] = O;
	  break;
	case 'T':
	  board[k+j*4] = T;
	  break;
	case '.':
	  board[k+j*4] = DOT;
	  break;
	default:
	  std::cout << "error at " << 2 + i * 5 + j << std::endl;
	  return -1;
	  break;
	}
      }
    }
    //    ifs >> buf;
    
    printBoard( board );
    Result r = calc( board );

    ofs << "Case #" << i+1 << ": ";
    switch(r) {
    case X_WON:
      ofs << "X won\r\n";
      break;
    case O_WON:
      ofs << "O won\r\n";
      break;
    case DRAW:
      ofs << "Draw\r\n";
      break;
    case NOT_COMPLETED:
      ofs << "Game has not completed\r\n";
      break;
    default:
      break;
    }
  }

}

Result calc( int board[] ) {
  // check diagonal
  int d1 = board[0] * board[5] * board[10] * board[15];
  int d2 = board[3] * board[6] * board[9] * board[12];
  if( d1 != 0 ) {
    if( board[0] == T ) {
      if( board[5] == board[10] && board[10] == board[15] ) return (board[5] == X) ? X_WON : O_WON;
    } else {
      int diff = board[0] - T;
      bool flg = true;
      for( int i = 1; i < 4; i++ ) {
	int idx = i*5;
	int cur_diff = board[idx] - T;
	if( diff * cur_diff < 0 ) {
	  flg = false;
	  break;
	}
      }
      if(flg) return (diff > 0) ? O_WON : X_WON;
    }
  }
  if( d2 != 0 ) {
    if( board[3] == T ) {
      if( board[6] == board[9] && board[9] == board[12] ) return (board[6] == X) ? X_WON : O_WON;
    } else {
      int diff = board[3] - T;
      bool flg = true;
      for( int i = 1; i < 4; i++ ) {
        int idx = 3 + i*3;
        int cur_diff = board[idx] - T;
        if( diff * cur_diff < 0 ) {
          flg = false;
          break;
        }
      }
      if(flg) return (diff > 0) ? O_WON : X_WON;
    }
  }


  // check row
  for( int i = 0; i < 4; i++ ) {
    int p = board[i*4] * board[i*4+1] * board[i*4+2] * board[i*4+3];
    if( p == 0 ) continue;
    if( board[i*4] == T ) {
      if( board[i*4+1] == board[i*4+2] && board[i*4+2] == board[i*4+3] ) return (board[i*4+1] == X) ? X_WON : O_WON;
    } else {
      int diff = board[i*4] - T;
      bool flg = true;
      for( int j = 1; j < 4; j++ ) {
	int idx = i*4 + j;
	int cur_diff = board[idx] - T;
	if( diff * cur_diff < 0 ) {
	  flg = false;
	  break;
	}
      }
      if(flg) return (diff > 0) ? O_WON : X_WON;
    }
  }

  // check column
  for( int i = 0; i < 4; i++ ) {
    int p = board[i] * board[i+4] * board[i+8] + board[i+12];
    if( p == 0 ) continue;
    if( board[i] == T ) {
      if( board[i+4] == board[i+8] && board[i+8] == board[i+12] ) return (board[i+4] == X) ? X_WON : O_WON;
    } else {
      int diff = board[i] - T;
      bool flg = true;
      for( int j = 1; j < 4; j++ ) {
        int idx = i + j*4;
        int cur_diff = board[idx] - T;
        if( diff * cur_diff < 0 ) {
          flg = false;
          break;
        }
      }
      if(flg) return (diff > 0) ? O_WON : X_WON;
    }
  }

  // check not_completed
  for( int i = 0; i < 16; i++ ) {
    if( board[i] == DOT ) return NOT_COMPLETED;
  }

  return DRAW;
}

void printBoard(int board[]) {
  for(int i = 0; i < 4; i++) {
    for(int j = 0; j < 4; j++) {
      if( board[j+i*4] == X ) std::cout << "X";
      if( board[j+i*4] == O ) std::cout << "O";
      if( board[j+i*4] == T ) std::cout << "T";
      if( board[j+i*4] == DOT ) std::cout << ".";
    }
    std::cout << std::endl;
  }
  std::cout << std::endl;
}
