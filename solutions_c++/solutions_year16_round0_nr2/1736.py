#if 1
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
using namespace std;

typedef long long LL;
typedef long double LD;
typedef pair<int , int> pii;
typedef vector <int> veci;
typedef vector <veci> graph;
const LD eps = 1e-9;
const LD pi = acos(-1.0);
const int inf = 1000 * 1000 * 1000;
const LL inf64 = LL(inf) * inf;

#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define iss istringstream
#define oss ostringstream
#define dbg(x) {cerr << #x << " = " << x << endl;}
#define dbgv(x) {cerr << #x << " ={"; for (int _i = 0; _i < x.size(); _i++) {if (_i) cerr << ", "; cerr << x[_i];} cerr << "}" << endl;}
#define NAME "problem"

template<class T> string to_str(const T &a) { oss os; os << a; return os.str(); }
template<> string to_str<LD>(const LD& a) { oss os; os.precision(10); os.setf(ios::fixed); os << a; return os.str(); }
template<class T> T from_str(const string &s) { iss is; T val; is >> val; return val; }
string T(int test) { ostringstream os; os << "Case #" << test << ":"; return os.str(); }
int _test_start = -1, _test_end = -1;
bool need_to_run(int test) { return _test_start == -1 || (_test_start <= test && test <= _test_end); }

map<string, int> was;

void apply(string& s, int top) {
  reverse(s.begin(), s.begin() + top);
  for (int i = 0; i < top; ++i) {
    char& ch = s[i];
    ch = (ch == '+') ? '-' : '+';
  }
}


int brute(const string& s) {
  was.clear();
  queue<string> q;
  q.push(s);
  was[s] = 0;

  while (!q.empty()) {
    auto cur = q.front();
    q.pop();
    // dbg(cur);
    if (cur.find('-') == string::npos) {
      break;
    }
    
    for (int i = 0; i < cur.size(); ++i) {
      string t = cur;
      apply(t, i + 1);
      // cerr << cur << "(" << i + 1 << "): " << t << endl;
      if (!was.count(t)) {
        was[t] = was[cur] + 1;
        q.push(t);
      }
    }
  }
  
  return was[string(s.size(), '+')];
}

int greedy(string s) {
  int res = 0;

  while (!s.empty()) {
    if (s[s.size() - 1] == '+') {
      s.resize(s.size() - 1);
    } else if (s[0] == '-') {
      ++res;
      apply(s, s.size());
    } else {
      ++res;

      int pos = s.find('-');
      if (pos == string::npos) {
        pos = s.size();
      }

      apply(s, pos);
    }
  }

  return res;
}

void solve(int test) {
	// read
  string s;
  cin >> s;

	if (!need_to_run(test)) return;
	// solve
//	cout << T(test) << " " << brute(s) << endl;
  cout << T(test) << " " << greedy(s) << endl;
	// write


}


void test() {
  for (int len = 1; len <= 10; ++len) {
    for (int i = 0; i < 1 << len; ++i) {
      string s;
      for (int j = 0; j < len; ++j) {
        if (i & (1 << j)) {
          s += "+";
        } else {
          s += "-";
        }
      }

      int brute_res = brute(s);
      int greedy_res = greedy(s);

      if (brute_res != greedy_res) {
        cout << "WA at: " << s << endl;
        cout << "expected: " << brute_res << endl;
        cout << "received: " << greedy_res << endl;
        exit(1);
      }
    }
    cout << len << " is OK" << endl;
  }
  exit(0);
}

int main(int argc, char *argv[]) {
//  dbg(brute("+-")); exit(0);
//  test();
	//freopen("input.txt", "r", stdin); //freopen("output.txt", "w", stdout);
	//freopen(NAME ".in","r",stdin); freopen(NAME ".out","w",stdout);
	if (argc == 2) { _test_start = _test_end = from_str<int>(argv[1]); }
	if (argc == 3) { _test_start = from_str<int>(argv[1]); _test_end = from_str<int>(argv[2]); }

	clock_t tstart = clock();
	
	int tests;
	scanf("%d", &tests);
	for(int test = 1; test <= tests; ++test) {
		clock_t tprev = clock();
		solve(test);
		if (need_to_run(test)) {
		//	dbg("elapsed for #" << test << ": " << (clock() - tprev) / LD(CLOCKS_PER_SEC));
		}
	}

	dbg("elapsed: " << (clock() - tstart) / LD(CLOCKS_PER_SEC));
	return 0;
}
/*************************
*************************/
#endif
