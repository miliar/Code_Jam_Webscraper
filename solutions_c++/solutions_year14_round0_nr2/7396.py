#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <iomanip>
#include <memory>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <bitset>
#include <queue>
using namespace std;

//conversion
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

//typedef
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long ll;

//container util
#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)

//constant
const double EPS = 1e-10;
const int MAXI = 1234567890;

//debug
#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;



void printList(vector<int>& v) {
  for (size_t i = 0; i < v.size(); i++) {
	cout << v[i] << " ";
  }
  cout << endl;
}

void printMatrix(vector< vector<int> >& v) {
  for (size_t i = 0; i < v.size(); i++) {
	printList(v[i]);
  }
  cout << endl;
}

inline double takeTime(double goal, double cpt) {
  return goal / cpt;
}

double solve1(int farm_count, double C, double F, double X) {
  double ans = 0;
  double cpt = 2;
  for (int i = 0; i < farm_count; i++) {
    ans += takeTime(C, cpt);
    cpt += F;
  }
  return ans + takeTime(X, cpt);
}

double solve(double C, double F, double X) {
  double ans = DBL_MAX;
  int farm_count = 0;
  while (true) {
    double t = solve1(farm_count, C, F, X);
    farm_count++;
    if (t < ans) ans = t;
    else return ans;
  }
  return ans;
}
int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    double C, F, X;
    cin >> C >> F >> X;
    double ans = solve(C, F, X);
    cout << "Case #" << i + 1 << ": ";
    cout << fixed << setprecision(8) << ans << endl;
  }
  return 0;
}
