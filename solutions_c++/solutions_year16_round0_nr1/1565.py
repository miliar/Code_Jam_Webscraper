#include <iostream>
#include <sstream>
#include <string>
#include <queue>
#include <deque>
#include <vector>
#include <list>
#include <map>
#include <functional>
#include <algorithm>
#include <iterator>
#include <set>
#include <stack>
#include <limits>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <numeric>


#define LL long long
#define LD long double
#define DD double
#define FORI(i,k,n) for (int i = (k); i < (n); i++)
#define RFORI(i,k,n) for (int i = (k); i > (n); i--)
#define FORLL(i,k,n) for (long long i = (k); i < (n); i++)
#define RFORLL(i,k,n) for (long long i = (k); i > (n); i--)
#define VI vector<int>
#define VPI vector<pair<int,int>>
#define VPL vector<pair<long long,long long>>
#define VB vector<bool>
#define VD vector<double>
#define VL vector<long long>
#define VS vector<string>
#define SZ(x) ((int)x.size())
#define VVI(f,x,y,val) vector<VI> f((x), VI((y), (val)))
#define VVB(f,x,y,val) vector<VB> f((x), VB((y), (val)))
#define VVL(f,x,y,val) vector<VL> f((x), VL((y), (val)))


using namespace std;

class Prob {

public:

  long solve(long N)
  {

    VB digitsSeen(10, false);

    long iter = N;
    while (true) {

      long count = iter;
      while (count > 0) {
        digitsSeen[count % 10] = true;
        count = count / 10;
      }

      if (std::count(digitsSeen.begin(), digitsSeen.end(), true) == 10)
        break;

      iter = iter + N;

    }

    return iter;
  }
};


int main() {
  int t;
  cin >> t;
  FORI(i,1,t+1) {

    long N;
    cin >> N;

    Prob t;
    if (N != 0) {
      long res = t.solve(N);
      cout << "Case #" << i << ": " << res << endl;
    }
    else {
      cout << "Case #" << i << ": " << "INSOMNIA" << endl;
    }
  }

  return 0;
}


