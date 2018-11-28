#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <stdexcept>

using namespace std;

#define REP(i, n) for(int i = 0; i<(n); i++)
#define abs(a) ((a) >= 0 ? (a) : -(a))
#define inf 2000000001
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VII;

typedef long long i64;
typedef unsigned long long u64;

int n;
VI v;


void print(string name, VI v) {
	// cout << name << ": " ;
	// REP(i, v.size()) cout << " " << v[i];
	// cout << endl;
}



void oneCase() {
	cin>>n;
	v = VI(n);
	REP(i, n) cin>>v[i];
	VI s = v;
	sort(s.begin(), s.end());
	int ret = 0;
	REP(i, s.size()) {
		auto k = find(v.begin(), v.end(), s[i]);
		int u = min(k - v.begin(), v.end() - 1 - k);
		ret += u;
		v.erase(k);
	}
	cout << ret;
}

int main() {
  int T;
  cin>>T;
  for (int t = 1; t <= T; t++) {
    cout << "Case #" << t << ": ";
    oneCase();
    cout << endl;
  }
}
