#include <iostream>
#include <fstream>
using namespace std;

int main() {
  int cases;
  int x, r, c;
  ifstream infile("D-small-attempt5.in", ios::in);
  ofstream outfile("D-small-attempt5.out", ios::out);

  infile >> cases;

  for (int i = 0; i < cases; i++) {
    infile >> x >> r >> c;
    outfile << "Case #" << i+1 << ": ";
    if ((r * c) % x != 0) {
      outfile << "RICHARD\n";
      continue;
    }
    if (x == 1 or x == 2) {
      outfile << "GABRIEL\n";
    } else if (x == 3) {
      if (r > 1 and c > 1){
        outfile << "GABRIEL\n";
      } else {
        outfile << "RICHARD\n";
      }
    } else if (x == 4 and r * c > 8 and (r > 2 and c > 2)) {
      outfile << "GABRIEL\n";
    } else {
      outfile << "RICHARD\n";
    }
  }
  infile.close();
  outfile.close();
}