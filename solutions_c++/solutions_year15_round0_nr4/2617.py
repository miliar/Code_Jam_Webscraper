#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>

using namespace std;

int main() {
 
  string line;
  ifstream fileToReadFrom;
  fileToReadFrom.open("/home/daeyeon/workspace/cpp/D-small-attempt1.in");

  ofstream fileToWriteTo;
  fileToWriteTo.open("/home/daeyeon/workspace/cpp/D-small-attempt.out");
  
  int numCase;
  int x,r,c;

    fileToReadFrom >> numCase;
    for (int i=0; i<numCase; i++) {
      // get the board size & number of connections needed to win
      fileToReadFrom >> x >> r >> c;
      if (x >=7 || (r*c)%x != 0 ||  (x!=2 && (r<=(x/2) || c<= (x/2)))) fileToWriteTo << "Case #" << i+1 << ": RICHARD" << endl;
      else fileToWriteTo << "Case #" << i+1 << ": GABRIEL" << endl;
 
    }
    
    fileToReadFrom.close();
    fileToWriteTo.close();
    return 0;
}
