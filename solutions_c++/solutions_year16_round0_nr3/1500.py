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


LL convBto10(LL num, LL base) {
  LL res = 0;
  LL cur_p = 1;
  while (num) {
    res += cur_p * (num & 1);
    cur_p *= base;
    num >>= 1;
  }
  
  return res;
}

bool check_div(LL num, int base, LL mod) {
  LL res = 0;
  LL cur_p = 1;
  while (num) {
    res += cur_p * (num & 1);
    res %= mod;
    cur_p *= base;
    cur_p %= mod;
    num >>= 1;
  }
  
  return res == 0;
}

LL find_div(LL num, int base) {
  for (LL i = 2; i < 10 && i < num; ++i) {
    if (check_div(num, base, i)) {
      return i;
    }
  }

  return -1;
}

vector<LL> get_divs(LL num) {
  vector<LL> divs;
  for (int i = 2; i <= 10; ++i) {
    LL d = find_div(num, i);
    if (d == -1) {
      return vector<LL>();
    }
    divs.pb(d);
  }
  return divs;
}

string get_str(LL num, int bits) {
  string res;
  for (int i = bits - 1; i >= 0; --i) {
    if (num & (1LL << i)) {
      res += "1";
    } else {
      res += "0";
    }
  }
  return res;
}

void print(int bits, int num) {
  for (LL i = (1LL << (bits - 1)) + 1; i < 1LL << bits; i += 2) {
    auto divs = get_divs(i);
    if (divs.empty()) {
      continue;
    }

    cout << get_str(i, bits);
    for (int d : divs) {
      cout << " " << d;
    }
    cout << endl;

    --num;

    if (num == 0) {
      break;
    }
  }
}

void solve(int test) {
	// read
  int n, j;
  cin >> n >> j;

	if (!need_to_run(test)) return;
	// solve
	cout << T(test) << endl;
  print(n, j);

	// write
}

int main(int argc, char *argv[]) {
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
