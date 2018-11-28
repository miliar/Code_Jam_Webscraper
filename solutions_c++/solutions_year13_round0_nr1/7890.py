#include <iostream>
#include <fstream>

using namespace std;

const int BOARD_SIZE = 4;


void showBoard(char board[][BOARD_SIZE]);
// 1, x win
// 2, 0 win
// 3, draw
// 4, not finish yet

int scanBoard(char board[][BOARD_SIZE]);


int main(int argc, char ** argv){
  ifstream inputFile;
  ofstream outputFile("output");
  if(argc < 2){
    cout << "Usage : " << argv[0] << " s/l" << endl;
    return 0;
  }
  
  if(argv[1][0] == 's'){
    inputFile.open("small");
  }else{
    inputFile.open("large");
  }

  if(inputFile.is_open() && outputFile.is_open()){
    int gameCount;
    string line;
    inputFile >> gameCount; 
    getline(inputFile, line);
    //gameCount = 1;
    for(int i = 1; i <= gameCount; i++){
      // read in 16 char and put them into a 2d array
      char board[BOARD_SIZE][BOARD_SIZE] = {0};
      for(int row = 0; row < BOARD_SIZE; row++){
	getline(inputFile, line);
	for(int col = 0; col < BOARD_SIZE; col++){
	  board[row][col] = line.at(col);
	  //cout << board[row][col] << " ";
	}
	//	cout << endl;
      }
      getline(inputFile, line);
      // the board has been initialized 
      int ret = scanBoard(board);
      string result;
      switch(ret){
      case 1:
	result = "X won";
	break;
      case 2:
	result = "O won";      
	break;
      case 3:
	result = "Draw";
	break;
      default:
	result = "Game has not completed";
	break;
      }
      cout << "Case #" << i << ": " << result << endl;
      outputFile << "Case #" << i << ": " << result << endl;
    }

    
  }else{
    cout << "Can't open file" << endl;
  }
  return 0;
}

int scanBoard(char board[][BOARD_SIZE]){
  bool hasDot = false;
  int winCount = 0;
  char player;
  
  // search horizontally
  for(int row = 0; row < BOARD_SIZE; row++){
    winCount = 0;
    for(int col = 0; col < BOARD_SIZE; col++){
      switch(board[row][col]){
      case 'T':
	winCount++;
	break;
      case 'X':
	winCount += 10;
	break;
      case '.':
	winCount += 5;
	hasDot = true;
	break;
      }
    }
    if(winCount > 35){
      cout << " h " << winCount << endl;
      return 1;
    }
    else if(winCount < 2){
      cout << " h " << winCount << endl;
      return 2;
    }
  }


  // search vertically
  for(int col = 0; col < BOARD_SIZE; col++){
    winCount = 0;
    for(int row = 0; row < BOARD_SIZE; row++){
      switch(board[row][col]){
      case 'T':
	winCount++;
	break;
      case 'X':
	winCount += 10;
	break;
      case '.':
	winCount += 5;
	hasDot = true;
	break;
      }
    }
    if(winCount > 35){
      cout << " v " << winCount << endl;
      return 1;
    }
    else if(winCount < 2){
      cout << " v " << winCount << endl;
      return 2;
    }
  }

  
  winCount = 0;
  // search diagonally down
  for(int row = 0; row < BOARD_SIZE; row++){
    switch(board[row][row]){
    case 'T':
      winCount++;
      break;
    case 'X':
      winCount += 10;
      break;
    case '.':
      winCount += 5;
      hasDot = true;
      break;
    }
  }
  if(winCount > 35){
    cout << " dd " << winCount << endl;
    return 1;
  }
  else if(winCount < 2){
    cout << " dd" << winCount << endl;
    return 2;
  }
  
  winCount = 0;
  // search diagonally up
  for(int row =0; row < BOARD_SIZE; row++){
    switch(board[row][BOARD_SIZE - 1 - row]){
    case 'T':
      winCount++;
      break;
    case 'X':
      winCount += 10;
      break;
    case '.':
      winCount += 5;
      hasDot = true;
      break;
    }
  }
    if(winCount > 35)
      return 1;
    else if(winCount < 2)
      return 2;
  
  // draw
  if(hasDot){
    return 4;
  }else{
    return 3;
  }
}



void showBoard(char board[][BOARD_SIZE]){
  for(int row = 0; row < BOARD_SIZE; row++){
    for(int col = 0; col < BOARD_SIZE; col++){
      cout << board[row][col];
    }
    cout << endl;
  }
  cout << endl;
}
