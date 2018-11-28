/*
ID: ahri1
PROG: B
LANG: C++
*/
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
#define sz(X) ((int)(X).size())
#define foreach(i,c) for(__typeof((c).begin()) i=((c).begin());i!=(c).end();++i)
template<class T> vector<T> tokenize_to(const string &str) { vector<T> r; T x; istringstream is(str); while (is >> x) r.push_back(x); return r; }
#define junik(X) {sort( (X).begin(), (X).end() ); (X).erase( unique( (X).begin(), (X).end() ), (X).end() ); }

/*

C <= 10000.
F <= 100.
X <= 100000.

*/

double totalTime(int numberOfFarms, double C, double F, double X){
  double coeff=0;
  for(int i=0;i<numberOfFarms;++i){
    coeff+=1.0/(2+i*F);
  }
  return C*coeff + X/(2+numberOfFarms*F);
}

double timeToGoal(double current, double F, double goal) {
  if (current >= goal) return 0;
  return (goal-current)/F;
}

void solve(){
  double C, F, X;
  cin >> C >> F >> X;
  double ret=X/2.0;
  
  int count = 1;
  double F_last = 0.5;
  double F_total = 0;
  double sol = 0;
  while (true) {
    F_total+=F_last;
    F_last=1/(2+ F*count++);
    //cout << F_total << " " << F_last << endl;
    sol=X*F_last + C*F_total;
    //cout << "new sol: " << sol << endl;
    if (sol>ret) break;
    ret=sol;
  }
  
  
  cout << fixed << ret  << endl;
}

int main() {

  cin.sync_with_stdio(0);
  cout.precision(8);
  int T;
  cin >> T;
  for (int i=0;i<T;i++) {
    cout << "Case #" << i+1 << ": ";
    solve();
  }
  
  return 0;
}
