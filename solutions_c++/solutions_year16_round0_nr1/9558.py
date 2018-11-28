#include <iostream>
#include <set>
#include <fstream>

using namespace std;

void id(set<int>& s, unsigned long d) {
  while (d > 0) {
    s.insert(d%10);
    d /= 10;
  }
}

int main() {
  
  ifstream in("A-large.in");
  
  ofstream out("A-large.out");
  
  int n;
  in >> n;
  for (int z = 1; z <= n; ++z) {
  unsigned long d, m;
  bool b = true;
  set<int> s;
  in >> d;
  // cout << "d : " << d << endl;
  m = d;
  for (int i = 0; i <= 222; ++i) {
    id(s, m);
    // cout << "s : " << s.size() << endl;
    if (s.size() >= 10) {
      b = false;
      out << "Case #" << z << ": " << m << endl;\
      break;
    }
    m += d;
  }
  if (b) {
    out << "Case #" << z << ": "  << "INSOMNIA" << endl;
  }
  }
  
  return 0;
}
