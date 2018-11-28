#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
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

void filter(int a, const VVI& matrix, vector<bool>& c) {
  for (size_t i = 0; i < 4; i++) {
    if ((int)i == a - 1) continue;
    for (size_t j = 0; j < 4; j++) {
      c[matrix[i][j]] = false;
    }
  }
}


int solve(int ans1, const VVI& first,
	  int ans2, const VVI& second) {
  vector<bool> c(17, true);
  c[0] = false;
  filter(ans1, first, c);
  filter(ans2, second, c);

  int count = 0;
  int ans = 0;
  for (size_t i = 0; i < 17; i++) {
    if (!c[i]) continue;
    ans = i;
    count++;
  }
  if (count > 1) return -1;
  if (count == 0) return -2;
  return ans;
}

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    int ans1;
    cin >> ans1;
    VVI first(4, VI(4, 0));
    for (int j = 0; j < 4; j++) {
      for (int k = 0; k < 4; k++) {
	cin >> first[j][k];
      }
    }

    int ans2;
    cin >> ans2;
    VVI second(4, VI(4, 0));
    for (int j = 0; j < 4; j++) {
      for (int k = 0; k < 4; k++) {
	cin >> second[j][k];
      }
    }
    int ans = solve(ans1, first, ans2, second);
    cout << "Case #" << i + 1 << ": ";
    if (ans == -1) {
      cout << "Bad magician!" << endl;
    } else if (ans == -2) {
      cout << "Volunteer cheated!" << endl;
    } else {
      cout << ans << endl;
    }
  }
  return 0;
}
