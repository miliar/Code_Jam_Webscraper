#include <iostream>
#include <fstream>
#include <string>

using namespace std;

const char* fi = "A-large.in";
const char* fo = "A-large.out";

void transform(string &s, int index, int k) {
  int end = index + k;
  for (; index < end; index++) {
    s[index] == '-' ? s[index] = '+' : s[index] = '-';
  }
}

int solve(string s, int k) {
  int result = 0;
  
  int i = 0;
  while (i < s.length()) {
    if (s[i] == '-') {
      if (i + k <= s.length()) {
        transform(s, i, k);
        result++;
      } else {
        return -1;
      }
    }
    i++;
  }

  return result;
}

int main(int argc, const char * argv[]) {
  ifstream fin;
  fin.open(fi);
  
  ofstream fout;
  fout.open(fo);
  
  int nTest;
  fin >> nTest;
  for (int i = 1; i <= nTest; i++) {
    string s;
    int k;
    fin >> s >> k;
    int result = solve(s, k);
    
    fout << "Case #" << i << ": ";
    result != -1 ? fout << result << endl : fout << "IMPOSSIBLE" << endl;
  }
  
  fin.close();
  fout.close();
  return 0;
}
