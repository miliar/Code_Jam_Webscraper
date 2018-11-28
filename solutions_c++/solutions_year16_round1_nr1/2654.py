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
  string solve(string s)
  {
    string ans;

    FORI(i, 0, SZ(s)) {
      if (s[i] - 'A' >= ans[0] - 'A') {
        ans = s[i] + ans;
      }
      else {
        ans.push_back(s[i]);
      }
    }

    return ans;
  }
};


int main() {
  int t;
  cin >> t;
  FORI(i, 1, t + 1) {

    string S;
    cin >> S;


    Prob prob;
    cout << "Case #" << i << ": ";
    cout<<prob.solve(S);
    cout << endl;
  }

  return 0;
}


