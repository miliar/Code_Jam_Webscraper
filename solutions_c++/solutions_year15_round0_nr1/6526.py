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
  ifstream in("sol1.in");
  ofstream out("sol1.out");
  int _c;
  in >> _c;

  for(int _cc = 1; _cc <= _c; ++_cc)	{
 //   cout << _cc << '\n';
    out << "Case #" << _cc << ": ";

    int maxS, sum = 0, friends = 0;
    string nShy;
    in >> maxS >> nShy;

    for (int i = 0; i <= maxS; ++i) {
      if (nShy[i] != '0') 
        if (i - (sum + friends) > 0) friends += i - (sum + friends);
      sum += nShy[i] - '0';
//      cout << i << " " << friends << " " << nShy[i] << " " << sum << '\n';
    }

    out << friends << '\n';
  }

  return 0;
}

