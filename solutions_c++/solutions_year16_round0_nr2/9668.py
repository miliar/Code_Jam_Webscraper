#include <iostream>
#include <set>
#include <string>
#include <fstream>

using namespace std;



int main() {

  ifstream in("B-large.in");
  
  ofstream out("B-large.out");
  
  int n;
  in >> n;

  for (int z = 1; z <= n; ++z) {
  
  string s;
  in >> s;
 
  char ls = s[0];
  int counter = 0;
  
  for (const auto& i : s) {
    if (i != ls) {
      ls = i;
      ++counter;
    }
  }

  if (ls == '-') {
    ++counter; 
  }

  out << "Case #" << z << ": " << counter << endl;
  
  }
  
  return 0;
}
