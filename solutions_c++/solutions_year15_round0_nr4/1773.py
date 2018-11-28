#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <set>
#include <vector>
#include <iterator>
using namespace std;

int main() {
  ifstream fin("in.txt");
  ofstream fout("out.txt");
  int cases = 0;
  fin >> cases;
  for (int i = 1; i <= cases; ++i) {
    int x, r, c;
    fin >> x >> r >> c;
    if ((r*c)%x || x > r*c)
      fout << "Case #" << i << ": " << "RICHARD\n";
    else if (x == 1)
      fout << "Case #" << i << ": " << "GABRIEL\n"; 
    else if (x == 2)
      if (r * c == 1 || r * c == 3)
        fout << "Case #" << i << ": " << "RICHARD\n";
      else 
        fout << "Case #" << i << ": " << "GABRIEL\n"; 
    else if (x == 3)
      if (r == 1 || c == 1 || (r * c == 8))
        fout << "Case #" << i << ": " << "RICHARD\n";
      else 
        fout << "Case #" << i << ": " << "GABRIEL\n"; 
    else if (x == 4)
      if (r * c == 12 || r * c == 16)
        fout << "Case #" << i << ": " << "GABRIEL\n"; 
      else 
        fout << "Case #" << i << ": " << "RICHARD\n";
  }
  fin.close();
  fout.close();
}
