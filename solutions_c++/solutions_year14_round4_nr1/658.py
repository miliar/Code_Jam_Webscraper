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


void oneCase() {
	int n, c;
	cin >> n >> c;
	VI f(n);
	REP(i, n) cin>>f[i];
	sort(f.begin(), f.end());
	int ret = 0;
	int mi = 0;
	for (int i = f.size() - 1; i >= mi; i--) {
		if (f[i] > c) throw "error";
		if (i > mi && f[i] + f[mi] <= c) {
			ret++;
			mi++;
		} else {
			ret++;
		}
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
