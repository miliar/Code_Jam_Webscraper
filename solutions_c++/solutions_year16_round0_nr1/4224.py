#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;

const char* fi = "A-large.in.txt";
const char* fo = "output-large.txt";
const int cycle[10] = {0, 10, 5, 10, 5, 2, 5, 10, 5, 10};

int n;
bool a[10];
void explore(int x);
void Solve(ofstream &fo);

int main(int argc, const char * argv[]) {
  int nTest;
  ifstream fin;
  fin.open(fi);
  
  ofstream fout;
  fout.open(fo);
  
  fin >> nTest;
  for (int i = 1; i <= nTest; i++) {
    fin >> n;
    fout << "Case #" << i << ": ";
    Solve(fout);
  }
  
  fout.close();
  return 0;
}

void Solve(ofstream &fo) {
  if (n == 0) {
    fo << "INSOMNIA" << endl;
  }
  
  for (int i = 0; i < 10; i++) a[i] = false;
  
  for (int cnt = 1; cnt <= 100; cnt++) {
    explore(n * cnt);
    
    bool ok = true;
    for (int i = 0; i < 10; i++) {
      if (!a[i]) { ok = false; break; }
    }
    
    if (ok) {
      fo << n * cnt << endl;
      break;
    }
  }
}

void explore(int x) {
  while (x > 0) {
    int digit = x % 10;
    a[digit] = true;
    x /= 10;
  }
}
