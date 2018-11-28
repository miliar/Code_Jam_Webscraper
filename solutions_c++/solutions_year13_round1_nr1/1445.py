#include <cstdlib>
#include <cmath>
#include <ctime>
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;



int main(int argc, char** argv) {
  
  ifstream I(argv[1]);
  ofstream O("output.txt");

  int T; I >> T;
  for (int t = 0; t < T; ++t) {

    int r; I >> r;
    int i; I >> i;

    int count = 0;
    while (i > 0) {

      i -= ((r + 1) * (r + 1)) - (r * r);

      r += 2;
      ++count;
    }
    
    if (i < 0) --count;

    O << "Case #" << (t + 1) << ": " << count << endl;
    //cout << "Case #" << (t + 1) << ": " << count << endl;
  }


  I.close();
  O.close();
  return 0;
}