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
  VL solve(int K, int C, int S)
  {
    VL res;

    long long incr = (long long )pow<long, long>(K, (C - 1));
    long long start = 1;
    FORI(i, 0, K) {
      res.push_back(start);
      start += incr;
    }

    return res;
  }
};


void print(VL& res) {
  for (auto s : res) {
    cout<<s<<" ";
  }
}

int main() {
  int t;
  cin >> t;
  FORI(i,1,t+1) {

    int K, C, S;
    cin >> K >> C >> S;

    Prob prob;
    cout << "Case #" << i << ": ";
    print(prob.solve(K, C, S));
    cout << endl;
  }

  return 0;
}


