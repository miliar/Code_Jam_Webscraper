#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <algorithm>
#include <numeric>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
using namespace std;

inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)

#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;

int main() {
  int t;
  cin >> t;
  REP(i,t){
    double c,f,x;
    cin >> c >> f >> x;
    double cps = 2.0;
    double tm = 0.0;
    while(1){
      double tm_buy = c / cps;
      if(c >= x || (x-c)/cps < x/(cps+f)){//not buy
	cout << "Case #"<<i+1<<": ";
	printf("%.7f\n",(tm + x/cps));
	break;
      }else{
	tm += tm_buy;
	cps += f;
      }
    }
  }


    return 0;
}
