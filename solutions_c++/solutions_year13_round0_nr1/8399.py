#include <fstream>
#include <iostream>
#include <cstdlib>

using namespace std;

const int kBoardSize=4;
char board[kBoardSize][kBoardSize];
int roundNumber=0;
bool someoneWon;

void displayBoard() {
  for (int x=0; x<kBoardSize; x++) {
    for (int y=0; y<kBoardSize; y++) {
      cout << board[x][y];
    } cout << endl;
  } cout << endl;
  return;
}

bool xWonVertical() {
  for (int y=0; y<kBoardSize-1; y++) {
    if ( (board[0][y]=='X' || board[0][y]=='T')
        && (board[1][y]=='X' || board[1][y]=='T')
        && (board[2][y]=='X' || board[2][y]=='T')
        && (board[3][y]=='X' || board[3][y]=='T')
      ) {someoneWon=true; return true;}
  }
  return false;
}

bool xWonHorizont() {
  for (int x=0; x<kBoardSize-1; x++) {
    if (
           (board[x][0]=='X' || board[x][0]=='T')
        && (board[x][1]=='X' || board[x][1]=='T')
        && (board[x][2]=='X' || board[x][2]=='T')
        && (board[x][3]=='X' || board[x][3]=='T')
      ) {someoneWon=true; return true;}
  }
  return false;
}

bool xWonDiaLeftRight() {
  if (
         (board[0][0]=='X' || board[0][0]=='T')
      && (board[1][1]=='X' || board[1][1]=='T')
      && (board[2][2]=='X' || board[2][2]=='T')
      && (board[3][3]=='X' || board[3][3]=='T')
      ) {someoneWon=true; return true;}
  return false;
}

bool xWonDiaRightLeft() {
  if (
         (board[3][0]=='X' || board[3][0]=='T')
      && (board[2][1]=='X' || board[2][1]=='T')
      && (board[1][2]=='X' || board[1][2]=='T')
      && (board[0][3]=='X' || board[0][3]=='T')
      ) {someoneWon=true; return true;}
  return false;
}

bool oWonVertical() {
  for (int o=0; o<kBoardSize-1; o++) {
    if ( (board[0][o]=='O' || board[0][o]=='T')
        && (board[1][o]=='O' || board[1][o]=='T')
        && (board[2][o]=='O' || board[2][o]=='T')
        && (board[3][o]=='O' || board[3][o]=='T')
      ) {someoneWon=true; return true;}
  }
  return false;
}

bool oWonHorizont() {
  for (int o=0; o<kBoardSize-1; o++) {
    if (
           (board[o][0]=='O' || board[o][0]=='T')
        && (board[o][1]=='O' || board[o][1]=='T')
        && (board[o][2]=='O' || board[o][2]=='T')
        && (board[o][3]=='O' || board[o][3]=='T')
      ) {someoneWon=true; return true;}
  }
  return false;
}

bool oWonDiaLeftRight() {
  if (
         (board[0][0]=='O' || board[0][0]=='T')
      && (board[1][1]=='O' || board[1][1]=='T')
      && (board[2][2]=='O' || board[2][2]=='T')
      && (board[3][3]=='O' || board[3][3]=='T')
      ) {someoneWon=true; return true;}
  return false;
}

bool oWonDiaRightLeft() {
  if (
         (board[3][0]=='O' || board[3][0]=='T')
      && (board[2][1]=='O' || board[2][1]=='T')
      && (board[1][2]=='O' || board[1][2]=='T')
      && (board[0][3]=='O' || board[0][3]=='T')
      ) {someoneWon=true; return true;}
  return false;
}

int main() {
  bool hasEmptyField=false;
  ifstream fp;
  fp.open("A-small-attempt0.in");
  
  int NumberOfRounds;
  fp >> NumberOfRounds;
  NumberOfRounds++;
  
  for (roundNumber=1; roundNumber<NumberOfRounds; roundNumber++) {
    someoneWon=false;
    hasEmptyField=false;
    
    //Load map
    for (int x=0; x<kBoardSize; x++) {
      for (int y=0; y<kBoardSize; y++) {
        fp >> board[x][y];
      }
    }
    //displayBoard();
    
    //Did X win?
    if (xWonVertical()) cout << "Case #" << roundNumber << ": X won\n";
    if (xWonHorizont()) cout << "Case #" << roundNumber << ": X won\n";
    if (xWonDiaLeftRight()) cout << "Case #" << roundNumber << ": X won\n";
    if (xWonDiaRightLeft()) cout << "Case #" << roundNumber << ": X won\n";

    //Did O win?    
    if (oWonVertical()) cout << "Case #" << roundNumber << ": O won\n";
    if (oWonHorizont()) cout << "Case #" << roundNumber << ": O won\n";
    if (oWonDiaLeftRight()) cout << "Case #" << roundNumber << ": O won\n";
    if (oWonDiaRightLeft()) cout << "Case #" << roundNumber << ": O won\n";
    
    if (someoneWon==false) {
      for (int x=0; x<kBoardSize; x++) {
        for (int y=0; y<kBoardSize; y++) {
          if (board[x][y]== '.') hasEmptyField=true;
        }
      }
      
      if (hasEmptyField==true) cout << "Case #" << roundNumber << ": Game has not completed\n";
      else cout << "Case #" << roundNumber << ": Draw\n";
    }
  } // end of nth game
    
    return 0;
}
