#include <iostream>

#include <fstream>

#include <string>

using namespace std;

char table [4][4];

int main(int argc, char *argv[])
{
  ifstream inputFile;
  inputFile.open(argv[1]);

  string numOfInputStr;
  getline(inputFile, numOfInputStr);
  int numOfInput = atoi(numOfInputStr.c_str());

  //cout << argv[1] << endl;
  //cout << numOfInput << endl;

  for(int lineIndex=0; lineIndex<numOfInput; lineIndex++) {

    int numOfSpaceFound = 0;

    for(int rowIndex=0; rowIndex<4; rowIndex++) {

      string line;
      getline(inputFile,line);

      for(int columnIndex=0; columnIndex<4; columnIndex++) {

	table[rowIndex][columnIndex] = line[columnIndex];

        if(line[columnIndex]=='.') {
          numOfSpaceFound++;
        }

      }
    }

    if(lineIndex<numOfInput-1) {
      string line;
      getline(inputFile,line);
    }

    bool foundWinner = false;

    for(int rowIndex=0; rowIndex<4&&!foundWinner; rowIndex++) {
      if((table[rowIndex][0]=='X'||table[rowIndex][0]=='T')&&(table[rowIndex][1]=='X'||table[rowIndex][1]=='T')&&(table[rowIndex][2]=='X'||table[rowIndex][2]=='T')&&(table[rowIndex][3]=='X'||table[rowIndex][3]=='T')) {
        cout << "Case #" << lineIndex+1 << ": " << "X won" << endl;
        foundWinner = true;
        break;
      } else if((table[rowIndex][0]=='O'||table[rowIndex][0]=='T')&&(table[rowIndex][1]=='O'||table[rowIndex][1]=='T')&&(table[rowIndex][2]=='O'||table[rowIndex][2]=='T')&&(table[rowIndex][3]=='O'||table[rowIndex][3]=='T')) {
        cout << "Case #" << lineIndex+1 << ": " << "O won" << endl;
        foundWinner = true;
        break;
      }
    }

    for(int columnIndex=0; columnIndex<4&&!foundWinner; columnIndex++) {
      if((table[0][columnIndex]=='X'||table[0][columnIndex]=='T')&&(table[1][columnIndex]=='X'||table[1][columnIndex]=='T')&&(table[2][columnIndex]=='X'||table[2][columnIndex]=='T')&&(table[3][columnIndex]=='X'||table[3][columnIndex]=='T')) {
        cout << "Case #" << lineIndex+1 << ": " << "X won" << endl;
        foundWinner = true;
        break;
      } else if((table[0][columnIndex]=='O'||table[0][columnIndex]=='T')&&(table[1][columnIndex]=='O'||table[1][columnIndex]=='T')&&(table[2][columnIndex]=='O'||table[2][columnIndex]=='T')&&(table[3][columnIndex]=='O'||table[3][columnIndex]=='T')) {
        cout << "Case #" << lineIndex+1 << ": " << "O won" << endl;
        foundWinner = true;
        break;
      }
    }

    if(!foundWinner) {
      if((table[0][0]=='X'||table[0][0]=='T')&&(table[1][1]=='X'||table[1][1]=='T')&&(table[2][2]=='X'||table[2][2]=='T')&&(table[3][3]=='X'||table[3][3]=='T')) {
        cout << "Case #" << lineIndex+1 << ": " << "X won" << endl;
        foundWinner = true;
      }
    }

    if(!foundWinner) {
      if((table[0][0]=='O'||table[0][0]=='T')&&(table[1][1]=='O'||table[1][1]=='T')&&(table[2][2]=='O'||table[2][2]=='T')&&(table[3][3]=='O'||table[3][3]=='T')) {
        cout << "Case #" << lineIndex+1 << ": " << "O won" << endl;
        foundWinner = true;
      }
    }

    if(!foundWinner) {
      if((table[0][3]=='X'||table[0][3]=='T')&&(table[1][2]=='X'||table[1][2]=='T')&&(table[2][1]=='X'||table[2][1]=='T')&&(table[3][0]=='X'||table[3][0]=='T')) {
        cout << "Case #" << lineIndex+1 << ": " << "X won" << endl;
        foundWinner = true;
      }
    }

    if(!foundWinner) {
      if((table[0][3]=='O'||table[0][3]=='T')&&(table[1][2]=='O'||table[1][2]=='T')&&(table[2][1]=='O'||table[2][1]=='T')&&(table[3][0]=='O'||table[3][0]=='T')) {
        cout << "Case #" << lineIndex+1 << ": " << "O won" << endl;
        foundWinner = true;
      }
    }

    if(!foundWinner&&numOfSpaceFound>0) {
      cout << "Case #" << lineIndex+1 << ": " << "Game has not completed" << endl;
      foundWinner = true;
    }

    if(!foundWinner) {
      cout << "Case #" << lineIndex+1 << ": " << "Draw" << endl;
    }

  }

  return 0;
} 
