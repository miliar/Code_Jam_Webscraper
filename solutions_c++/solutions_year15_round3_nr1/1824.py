/*
 * ships.cc
 *
 *  Created on: May 10, 2015
 *      Author: maciek
 */

#include <fstream>
#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <sstream>
#include <stack>
#include <map>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[]){

  ifstream fs(argv[1]);
  int T, R, C, W;
  string s;

  getline(fs, s);
  istringstream(s) >> T;
  for(int i = 0; i < T; i++){
	  getline(fs, s);
	  istringstream(s) >> R >> C >> W;
	  int x = C/W;
	  int y = C % W;
	  if (!y)
		  cout << "Case #" << i+1 << ": " << (R-1)*x + (x+W-1)*R << endl;
	  else
		  cout << "Case #" << i+1 << ": " << (R-1)*x + (x+W)*R << endl;
  }
}
