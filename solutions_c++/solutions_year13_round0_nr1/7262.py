#include <iostream>
#include <fstream>
#include <cstdio>
#include <stdlib.h>
#include <string.h>
#include <string>

using namespace std;
int main() {
  int testcases = 0;
  /*char filename[] = "A-small.in";
  std::ifstream fileRead;
  fileRead.open(filename, ios::in);
  if(!fileRead.is_open()) {
    std::cout <<"Failed to open file:" << filename << std::endl;
    return 0;
  }*/
  char line[10000];
  memset(line, '\0', 10000);  
  //fileRead.getline(line, 10000);
  //testcases = atoi(line);
  std::cin >> testcases;
  for(int testcase=0; testcase < testcases; ++testcase) {
    memset(line, '\0', 10000);
    bool isempty = false;
    char matrix[4][4];
    for(int rows = 0; rows < 4; ++rows) {
      for(int cols =0; cols < 4; ++cols) {
        //fileRead >> matrix[rows][cols];
          std::cin >> matrix[rows][cols];
          if(matrix[rows][cols] == '.')
            isempty = true;
      }
      //fileRead.getline(line, 10000);
    }
    bool x_won = false;
    bool o_won = false;
    for(int rows =0; rows < 4; ++rows) {
      if(matrix[rows][0] == 'X' && matrix[rows][1] == 'X' && matrix[rows][2] == 'X' && (matrix[rows][3] == 'X' || matrix[rows][3] == 'T'))
        x_won = true;
      if(matrix[rows][0] == 'X' && matrix[rows][1] == 'X' && (matrix[rows][2] == 'X' || matrix[rows][2] == 'T') && matrix[rows][3] == 'X')
          x_won = true;
      if(matrix[rows][0] == 'X' && (matrix[rows][1] == 'X' || matrix[rows][1] == 'T') && matrix[rows][2] == 'X' && matrix[rows][3] == 'X')
          x_won = true;
      if((matrix[rows][0] == 'X' || matrix[rows][0] == 'T') && matrix[rows][1] == 'X' && matrix[rows][2] == 'X' && matrix[rows][3] == 'X')
          x_won = true;
      
      if(matrix[rows][0] == 'O' && matrix[rows][1] == 'O' && matrix[rows][2] == 'O' && (matrix[rows][3] == 'O' || matrix[rows][3] == 'T'))
        o_won = true;
      if(matrix[rows][0] == 'O' && matrix[rows][1] == 'O' && (matrix[rows][2] == 'O' || matrix[rows][2] == 'T') && matrix[rows][3] == 'O')
        o_won = true;
      if(matrix[rows][0] == 'O' && (matrix[rows][1] == 'O' || matrix[rows][1] == 'T') && matrix[rows][2] == 'O' && matrix[rows][3] == 'O')
        o_won = true;
      if((matrix[rows][0] == 'O' || matrix[rows][0] == 'T') && matrix[rows][1] == 'O' && matrix[rows][2] == 'O' && matrix[rows][3] == 'O')
        o_won = true;
    }
    
    for(int cols =0; cols < 4; ++cols) {
      if(matrix[0][cols] == 'X' && matrix[1][cols] == 'X' && matrix[2][cols] == 'X' && (matrix[3][cols] == 'X' || matrix[3][cols] == 'T'))
        x_won = true;
      if(matrix[0][cols] == 'X' && matrix[1][cols] == 'X' && (matrix[2][cols] == 'X' || matrix[2][cols] == 'T') && matrix[3][cols] == 'X')
        x_won = true;
      if(matrix[0][cols] == 'X' && (matrix[1][cols] == 'X' || matrix[1][cols] == 'T') && matrix[2][cols] == 'X' && matrix[3][cols] == 'X')
        x_won = true;
      if((matrix[0][cols] == 'X' || matrix[0][cols] == 'T') && matrix[1][cols] == 'X' && matrix[2][cols] == 'X' && matrix[3][cols] == 'X')
        x_won = true;
      
      if(matrix[0][cols] == 'O' && matrix[1][cols] == 'O' && matrix[2][cols] == 'O' && (matrix[3][cols] == 'O' || matrix[3][cols] == 'T'))
        o_won = true;
      if(matrix[0][cols] == 'O' && matrix[1][cols] == 'O' && (matrix[2][cols] == 'O' || matrix[2][cols] == 'T') && matrix[3][cols] == 'O')
        o_won = true;
      if(matrix[0][cols] == 'O' && (matrix[1][cols] == 'O' || matrix[1][cols] == 'T') && matrix[2][cols] == 'O' && matrix[3][cols] == 'O')
        o_won = true;
      if((matrix[0][cols] == 'O' || matrix[0][cols] == 'T') && matrix[1][cols] == 'O' && matrix[2][cols] == 'O' && matrix[3][cols] == 'O')
        o_won = true;
    }
    
    if(matrix[0][0] == 'X' && matrix[1][1] == 'X' && matrix[2][2] == 'X' && (matrix[3][3] == 'X' || matrix[3][3] == 'T'))
      x_won = true;
    if(matrix[0][0] == 'X' && matrix[1][1] == 'X' && (matrix[2][2] == 'X' || matrix[2][2] == 'T') && matrix[3][3] == 'X')
      x_won = true;
    if(matrix[0][0] == 'X' && (matrix[1][1] == 'X' || matrix[1][1] == 'T') && matrix[2][2] == 'X' && matrix[3][3] == 'X')
      x_won = true;
    if((matrix[0][0] == 'X' || matrix[0][0] == 'T') && matrix[1][1] == 'X' && matrix[2][2] == 'X' && matrix[3][3] == 'X')
      x_won = true;

    if(matrix[0][0] == 'O' && matrix[1][1] == 'O' && matrix[2][2] == 'O' && (matrix[3][3] == 'O' || matrix[3][3] == 'T'))
      o_won = true;
    if(matrix[0][0] == 'O' && matrix[1][1] == 'O' && (matrix[2][2] == 'O' || matrix[2][2] == 'T') && matrix[3][3] == 'O')
      o_won = true;
    if(matrix[0][0] == 'O' && (matrix[1][1] == 'O' || matrix[1][1] == 'T') && matrix[2][2] == 'O' && matrix[3][3] == 'O')
      o_won = true;
    if((matrix[0][0] == 'O' || matrix[0][0] == 'T') && matrix[1][1] == 'O' && matrix[2][2] == 'O' && matrix[3][3] == 'O')
      o_won = true;


    if(matrix[0][3] == 'X' && matrix[1][2] == 'X' && matrix[2][1] == 'X' && (matrix[3][0] == 'X' || matrix[3][0] == 'T'))
      x_won = true;
    if(matrix[0][3] == 'X' && matrix[1][2] == 'X' && (matrix[2][1] == 'X' || matrix[2][1] == 'T') && matrix[3][0] == 'X')
      x_won = true;
    if(matrix[0][3] == 'X' && (matrix[1][2] == 'X' || matrix[1][2] == 'T') && matrix[2][1] == 'X' && matrix[3][0] == 'X')
      x_won = true;
    if((matrix[0][3] == 'X' || matrix[0][3] == 'T') && matrix[1][2] == 'X' && matrix[2][1] == 'X' && matrix[3][0] == 'X')
      x_won = true;

    if(matrix[0][3] == 'O' && matrix[1][2] == 'O' && matrix[2][1] == 'O' && (matrix[3][0] == 'O' || matrix[3][0] == 'T'))
      o_won = true;
    if(matrix[0][3] == 'O' && matrix[1][2] == 'O' && (matrix[2][1] == 'O' || matrix[2][1] == 'T') && matrix[3][0] == 'O')
      o_won = true;
    if(matrix[0][3] == 'O' && (matrix[1][2] == 'O' || matrix[1][2] == 'T') && matrix[2][1] == 'O' && matrix[3][0] == 'O')
      o_won = true;
    if((matrix[0][3] == 'O' || matrix[0][3] == 'T') && matrix[1][2] == 'O' && matrix[2][1] == 'O' && matrix[3][0] == 'O')
      o_won = true;
    
    if( x_won )
      std::cout << "Case #" << testcase+1 <<": X won" << std::endl;
    else if( o_won)
      std::cout << "Case #" << testcase+1 <<": O won" << std::endl;
    else if( isempty)
      std::cout << "Case #" << testcase+1 <<": Game has not completed" << std::endl;
    else
      std::cout << "Case #" << testcase+1 <<": Draw" << std::endl;
  }
  return 0;
}










