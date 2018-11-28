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

typedef bitset<8> B;

int M, N;
VS v;
vector<VS> prefixs;

i64 X, Y;

i64 getNum(B s) {
	set<string> temp;
	REP(i, M) if (s[i]) {
		temp.insert(prefixs[i].begin(), prefixs[i].end());
	}
	return temp.size();
}

void go(B rest, vector<B>& path) {
	if (path.size() == N) {
		i64 num = 0;
		REP(i, N) {
			num += getNum(path[i]);
		}
		if (X < num) {
			X = num;
			Y = 1;
		}  else if (X == num) {
			Y++;
		}
		return;
	}
	if (!rest.any()) {
		return;
	}
	if (path.size() == N - 1) {
		path.push_back(rest);
		go(rest, path);
		path.pop_back();
		return;
	}
	REP(next, (1<<M)) if (next) {
		B nx(next);
		if ((nx & rest) == nx) {
			path.push_back(nx);
			go(rest ^ nx, path);
			path.pop_back();
		}
	}
}
	
void oneCase() {
	cin >> M >> N;
	v = VS(M);
	prefixs = vector<VS>(M);
	REP(i, M) {
		cin >> v[i];
		REP(j, v[i].size() + 1) {
			prefixs[i].push_back(string(v[i].begin(), v[i].begin() + j));
		}
	} 
	
	X = Y = 0;
	B rest((1<<M) - 1);
	vector<B> path;
	go(rest, path);
	cout << X << ' ' << Y;
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
