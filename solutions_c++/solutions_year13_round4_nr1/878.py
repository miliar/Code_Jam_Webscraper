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


int fee(int d, int N) {
  return d * (2 * N - d + 1) / 2;
}

int calc_orig(int N, int M, const vector< pair<PII, int> >& v) {
  int sum = 0;
  for (size_t i = 0; i < v.size(); i++) {
    sum += fee(v[i].first.second - v[i].first.first, N) * v[i].second;
  }
  return sum;
}


int solve(int N, int M, const vector< pair<PII, int> >& v) {
  const int orig = calc_orig(N, M, v);

  vector<int> pass(N + 1, 0);

  for (size_t i = 0; i < v.size(); i++) {
    int t_in = v[i].first.first;
    int t_out = v[i].first.second;
    int t_p = v[i].second;
    for (int j = t_in; j < t_out; j++) {
      pass[j] += t_p;
    }
  }

  int sum = 0;
  while (true) {
    int start = -1;
    int end = -1;
    int maxv = -1;
    for (int i = 1; i < N + 1; i++) {
      if (pass[i] == 0) {
	if (start == -1) continue;
	end = i - 1;
	sum += fee(end - start + 1, N) * maxv;
	for (int j = start; j <= end; j++) {
	  pass[j] -= maxv;
	}
	break;
      } else {
	if (start == -1) {
	  start = i;
	  maxv = pass[i];
	  continue;
	} else {
	  maxv = min(maxv, pass[i]);
	  continue;
	}
      }
    }
    if (start == -1 && end == -1) return orig - sum;
    if (end == -1) {
      sum += fee(N - start + 1, N) * maxv;
      for (int j = start; j <= N; j++) {
	pass[j] -= maxv;
      }
    }
  }
  return 0;
}

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    int N, M;
    cin >> N >> M;
    vector< pair<PII, int> > v;
    for (int j = 0; j < M; j++) {
      pair<PII, int> p;
      cin >> p.first.first >> p.first.second >> p.second;
      v.PB(p);
    }
    int ans = solve(N, M, v);
    cout << "Case #" << i + 1 << ": " << ans << endl;
  }
  return 0;
}
