#include <string>
#include <iostream>
#include <sstream>
#include <stdio.h>
using namespace std;

bool results[3][4][4] = {
  {
    {false, true, false, true},
    {true, true, true, true},
    {false,	true,	false, true},
    {true,	true,	true,	true}
  },
  {
    {false, false, false, false},
    {false, false, true, false},
    {false, true, true, true},
    {false, false, true, false},
  },
  {
    {false, false, false, false},
    {false, false, false, false},
    {false, false, false, true},
    {false, false, true, true}
  },
};

int main (int argc, char const *argv[])
{
  string format = "Case #%d: %s\n";
  stringstream parse;
  string stringIn;
  int numCases;
  
  getline(cin, stringIn);
  numCases = atoi(stringIn.c_str());

  for(int i = 0; i < numCases; i++) {
    int x, r, c;
    bool win;

    // parse the line into x, r and c
    getline(cin, stringIn);
    parse.clear();
    parse.str("");
    parse << stringIn;
    parse >> x;
    parse >> r;
    parse >> c;

    if(x < 2){
      win = true;
    } else {
      win = results[x-2][r-1][c-1];
    }

    printf(format.c_str(), i + 1, win ? "GABRIEL" : "RICHARD");
  }

  return 0;
}