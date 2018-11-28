#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <string>
#include <ctime>
#include <cstdlib>
using namespace std;

int main() {
  ifstream fin("in.txt");
  ofstream fout("out.txt");

  int cases = 0;
  fin >> cases;
  for (int i = 1; i <= cases; ++i) {
    int smax;
    int y = 0;
    string si;
    fin >> smax >> si;
    int standing = 0;
    for (int j = 0; j < si.size(); ++j) {
      if (standing < j && si[j] - '0') {
        y += j - standing;
        standing += j - standing;
      }
      standing += si[j] - '0';
    }
    fout << "Case #" << i << ": ";
    fout << y;
    fout << endl;
  }
  fin.close();
  fout.close();
}
