#include <iostream>
#include <fstream>

using namespace std;

int t;
int c1, c2;
int myorig[4][4], mynew[4][4];
int myans = 0;
int mycount = 0;

int main(){
  ifstream fin ("A-small-attempt0.in");
  
  fin >> t;
  
  for (int x = 0; x < t; ++x){
    mycount = 0;
  
    fin >> c1;
    c1 -= 1;
    for (int i = 0; i < 4; ++i){
      for (int j = 0; j < 4; ++j){
	fin >> myorig[i][j];
      }
    }
    
    fin >> c2;
    c2 -= 1;
    for (int i = 0; i < 4; ++i){
      for (int j = 0; j < 4; ++j){
	fin >> mynew[i][j];
      }
    }
    
    for (int i = 0; i < 4; ++i){
      for (int j = 0; j < 4; ++j){
	if (myorig[c1][i] == mynew[c2][j]){
	  mycount += 1;
	  myans = myorig[c1][i];
	}
      }
    }
    
    cout << "Case #" << x + 1 << ": ";
    
    if (mycount > 1){
      cout << "Bad magician!" << endl;
    }
    else if (mycount == 0){
      cout << "Volunteer cheated!" << endl;
    }
    else {
      cout << myans << endl;
    }
    
  }
  
  
  return 0;


}