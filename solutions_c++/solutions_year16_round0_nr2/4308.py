#include <iostream>
#include <fstream>
#include <string>
using namespace std;

const char* fi = "B-large.in.txt";
const char* fo = "output-large.txt";
const int maxn = 101;

int a[maxn];
string s;

void Solve(ofstream &fo);

int main(int argc, const char * argv[]) {
  ifstream fin;
  fin.open(fi);
  ofstream fout;
  fout.open(fo);
  
  int nTest;
  fin >> nTest;
  for (int i = 1; i <= nTest; i++) {
    fin >> s;
    fout << "Case #" << i << ": ";
    Solve(fout);
  }

  fout.close();
  return 0;
}

void Solve(ofstream &fo) {
  for (int i = 0; i < s.length() + 1; i++) {
    a[i] = 0;
  }

  for (int i = 0; i < s.length(); i++) {
    if ((s[i] == '-' && i == 0) || (s[i] == '-' && s[i - 1] == '+')) {
      int aIndex = i + 1;
      if (i == 0) { a[aIndex] = 1; }
      else if (a[aIndex - 1] == 0 && s[i - 1] == '+') { a[aIndex] = 2; }
      else { a[aIndex] = a[aIndex - 1] + 2; }
    } else {
      int aIndex = i + 1;
      a[aIndex] = a[aIndex - 1];
    }
  }

  fo << a[s.length()] << endl;
}
