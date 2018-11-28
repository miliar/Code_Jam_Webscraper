#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <set>
#include <sstream>
#include <numeric>
#include <bitset>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cctype>
#include <cassert>
using namespace std;

typedef long long ll;
static const double EPS = 1e-8;
static const double PI = 4.0 * atan(1.0);
bool ISINT(double x){return fabs(x-(int)round(x))<EPS;}
bool ISEQ(double x,double y){return fabs(x-y)<EPS;}
string itos(ll x){stringstream ss;ss<<x;return ss.str();}
#define REP(i,a,b) for(int i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
#define EREP(i,a,b) for(int i=a;i<=b;i++)
#define erep(i,n) EREP(i,0,n)
#define foreach(itr,c) for(__typeof(c.begin()) itr=c.begin();itr!=c.end();itr++)

int main(void){
  int T;
  cin >> T;

  for(int CASE = 1; CASE <= T; CASE++){
    cout << "Case #" << CASE << ": ";

    set<int> st;
    for(int i = 1; i <= 16; i++){
      st.insert(i);
    }

    for(int k = 0; k < 2; k++){
      int a;
      cin >> a;

      for(int i = 1; i <= 4; i++){
        for(int j = 1; j <= 4; j++){
          int x;
          cin >> x;

          if(i != a){
            st.erase(x);
          }
        }
      }
    }

    if(st.size() == 1){
      cout << *(st.begin()) << endl;
    }
    else if(st.size() > 1){
      cout << "Bad magician!" << endl;
    }
    else{
      cout << "Volunteer cheated!" << endl;
    }
  }
}
