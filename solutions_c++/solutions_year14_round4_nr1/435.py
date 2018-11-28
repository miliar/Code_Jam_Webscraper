#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <utility>
#include <map>
#include <set>
#include <utility>

#define ALL(v) v.begin(), v.end()

using namespace std;
typedef long long ll;

template< typename T > T next() {  T tmp; cin >> tmp; return tmp; }

void dec(map< int, int > & f, int key) {
	f[key]--;
	if (f[key] == 0) {
		f.erase(key);
	}
}

void solve() {
	int n = next< int >();
	int x = next< int >();
	map< int, int > f;
	for (int i = 0; i < n; ++i) {
		f[ next< int >() ]++;		
	}
	int discs = 0;
	while (f.size() > 0) {
		int key = f.rbegin() -> first;
		dec(f, key);
		int up = x - key;
		map< int, int > :: iterator it = f.upper_bound(up);
		if (it != f.begin()) {
			--it;
			dec(f, it -> first);
		}
		discs++;
	}
	cout << discs << endl;
}

int main() {

//  freopen("input.txt", "rt", stdin);
//  freopen("output.txt", "wt", stdout);

  int test = next< int >();
  for (int i = 1; i <= test; ++i) {
    printf("Case #%d: ", i);
    solve();
  }

  return 0;
}

 