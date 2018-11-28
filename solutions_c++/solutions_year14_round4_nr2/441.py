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
	vector< int > a(n);
	generate(a.begin(), a.end(), next< int >);
	vector< int > s(a);
	sort(s.begin(), s.end());
	int left = 0;
	int right = (int)s.size() - 1;
	int sum = 0;
	for (size_t i = 0; i < s.size(); ++i) {
		int v = s[i];
		size_t pos = find(a.begin(), a.end(), v) - a.begin();
		sum += min(pos - left, right - pos);
		if (pos - left < right - pos) {
			for (size_t j = pos; j > left; --j) {
				a[j] = a[j - 1];
			}
			a[left++] = v;
		} else {
			for (size_t j = pos; j < right; ++j) {
				a[j] = a[j + 1];
 			}
			a[right--] = v;
		}
	}
	cout << sum << endl;
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

 