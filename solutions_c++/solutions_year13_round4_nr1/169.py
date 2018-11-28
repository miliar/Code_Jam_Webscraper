/* Opgave: A */
// 7+8+7=22 includes
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <climits>
#include <cassert>

#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <string>

#include <iostream>
#include <sstream>
#include <utility>
#include <functional>
#include <limits>
#include <numeric>
#include <algorithm>

using namespace std;

const long long MOD =  1000002013;
void doit (int t) {
  long long N, M;
  cin >> N >> M;
  map<int, long long> exiting;
  map<int, long long> entering;
  set<int> interesting;
  long long rc = 0;
  for(int i = 0; i < M; ++i) {
    long long a, b, c;
    cin >> a >>b >> c;
    entering[a] += c;
    exiting[b] += c;
    interesting.insert(a);
    interesting.insert(b);
    rc = (rc + c * (((b-a) * (2*N - b + a + 1) / 2) % MOD)) % MOD;
  }
  vector<pair<int, long long>> have;
  long long cost = 0;
  for(auto c : interesting) {
    have.push_back(make_pair(c, entering[c]));

    long long e = exiting[c];
    while(e > 0) {
      int d = c - have.back().first;
      long long cc = (d * (2*N - d + 1) / 2) % MOD; 
      if(have.back().second <= e) {
	e -= have.back().second;
	cost = (cost + have.back().second * cc) % MOD;
	have.pop_back();
      } else {
	have.back().second -= e;
	cost = (cost + e * cc) % MOD;
	e = 0;
      }
    }
  }
  cout << "Case #" << t << ": " << (rc + MOD - cost) % MOD << endl;
}

int main () {
	int t;
	cin >> t; //scanf ("%d ", &t);
	for (int i = 0; i < t; i++) {
		doit (i+1);
	}
	return 0;
}
/* Opgave: A */
