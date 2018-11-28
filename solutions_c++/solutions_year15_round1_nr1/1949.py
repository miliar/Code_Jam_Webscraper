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

const int N = 1000;

double mush[N];

int main()
{
  ios_base::sync_with_stdio(false);
  ifstream in("sol1.in");
  ofstream out("sol1.out");
  int _c;
  in >> _c;

  for(int _cc = 1; _cc <= _c; ++_cc)	{
    out << "Case #" << _cc << ": ";

    int n;
    in >> n;

    for (int i = 0; i < n; ++i) {
      in >> mush[i];
    }

    double m1 = 0, m2 = 0;

    for (int i = 1; i < n; ++i) {
      if (mush[i] < mush[i - 1]) 
        m1 += mush[i - 1] - mush[i];
    }
    
    double rate = 0;
    for (int i = 1; i < n; ++i) {
      if (rate < mush[i - 1] - mush[i])
        rate = mush[i - 1] - mush[i];
    }
//    rate /= 10;
//      cout << rate << endl;

    for (int i = 1; i < n; ++i) {
      m2 += min(mush[i - 1], rate);
    }

    out << int(m1 + .5) << " " << int(m2 + .5) << '\n';
  }

  return 0;
}

