#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath>
#include <string>
#include <algorithm>
#include <sstream>
#include <iomanip>
#include <utility>
#include <set>
#include <map>
#include <cctype>

#define FOR(i,n) for(long long int i=0; i<n; i++)
#define MP(a,b) make_pair(a,b)
#define PB(x) push_back(x)
#define SORT(a) sort(a.begin(), a.end())
#define REV(a) reverse(a.begin(), a.end())

#define COND(p,t,f) ((p)?(t):(f))

#define PI 3.14159265

using namespace std;
typedef long long int lint;
typedef unsigned long long int ulint;



int main() {
  int T;
  cin >> T;
  FOR(t,T) {
    double C,F,X;
    cin >> C >> F >> X;
    vector<double> B;
    vector<double> T;
    B.PB(0);
    T.PB(X/2.0);
    int i=0;
    while(1) {
      i++;
      B.PB(B[i-1]+C/(2+F*(i-1)));
      double nT = B[i] + X/(2+F*i);
      if (nT>T.back()) break;
      else T.PB(nT);
    }
    cout << "Case #" << t+1 << ": ";
    cout << setprecision(30) << T.back() << endl;
  }
  
}