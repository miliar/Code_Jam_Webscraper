#include <iostream>
#include <fstream>
#include <cmath>
#include <sstream>

using namespace std;

bool pol(unsigned int num){
  stringstream tmp;
  tmp << num;
  unsigned int length = tmp.str().length();
  for (int i=0; i<length/2; ++i)
    if (tmp.str().at(i) != tmp.str().at(length-i-1))
      return false;
  return true;
}

unsigned int round(double num){
  unsigned int res = static_cast<unsigned int>(num);
  if (num - res > 0.5) ++res;
  return res;
}

int main(){
  ifstream in("C:/CodeJam/3/C-small-attempt0.in");
  ofstream out("C:/CodeJam/3/res.txt");
  //cin.rdbuf(in.rdbuf());
  //cout.rdbuf(out.rdbuf());
  unsigned int T;
  in >> T;
  for (unsigned int t = 0; t < T; ++t){
    unsigned int A,B;
    in >> A >> B;
    unsigned int count = 0;
    for (unsigned int cur = A; cur <= B; ++cur){
      if (pol(cur)){
        double sq = sqrt(cur);
        unsigned int r = round(sq);
        if (r*r == cur)
          if (pol(r))
            ++count;
      }
    }
    out << "Case #" << t + 1 << ": " << count << endl;
  }
  in.close();
  out.close();
}