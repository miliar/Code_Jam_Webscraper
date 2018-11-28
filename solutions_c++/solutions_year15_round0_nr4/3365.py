#include<algorithm>
#include<bitset>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<cstdio>
#include<deque>
#include<fstream>
#include<iostream>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<sstream>
#include<stack>
#include<string>
#include<utility>
#include<vector>

using namespace std;

int main()
{
  ios_base::sync_with_stdio(false);
  ifstream in("sol4.in");
  ofstream out("sol4.out");
  int _c;
  in >> _c;

  for(int _cc = 1; _cc <= _c; ++_cc)	{
    out << "Case #" << _cc << ": ";
    
    int x, r, c;
    in >> x >> r >> c;

    if (x == 1) out << "GABRIEL";
    else if (x == 2) {
      if (r % 2 == 0 || c % 2 == 0) {
        out << "GABRIEL";
      } else {
        out << "RICHARD";
      }
    } else if (x == 3) {
      if (r >= 2 && c >= 2 && (r == 3 || c == 3)) {
        out << "GABRIEL"; 
      } else {
        out << "RICHARD";
      }
    } else {
      if (r >= 3 && c >= 3 && (r == 4 || c == 4)) {
        out << "GABRIEL";
      } else {
        out << "RICHARD";
      }
    }
    
    out << '\n';
  }

  return 0;
}

