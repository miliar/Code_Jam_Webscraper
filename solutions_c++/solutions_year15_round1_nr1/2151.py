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
#include <iomanip>
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
#define foreach(itr,c) for(__typeof(c.begin()) itr=c.begin();itr!=c.end();itr++)

int t[1002];

int main(void){
  int T;
  cin >> T;

  for (int CASE = 1; CASE <= T; CASE++) {
    cout << "Case #" << CASE << ": ";

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
      cin >> t[i];
    }

    int ansA = 0;
    int eat = 0;

    for (int i = 0; i < n - 1; i++) {
      ansA += max(0, t[i] - t[i + 1]);
      eat = max(eat, max(0, t[i] - t[i + 1]));
    }

    int ansB = 0;

    for (int i = 0; i < n - 1; i++) {
      ansB += min(t[i], eat);
    }

    cout << ansA << " " << ansB << endl;
  }
}
