#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cassert>

using namespace std;

typedef pair<char, int> P;

void validate(const vector<P>& v) {
  int s = 0;
  for (auto& p : v) {
    s += p.second;
  }
  for (auto& p : v) {
    if (p.second*2 > s) {
      assert(false);
    }
  }
}

int main() {
  cin.sync_with_stdio(false);
  cout.sync_with_stdio(false);
  size_t N;
  cin >> N;
  for (size_t k = 1; k <= N; ++k) {
    size_t n;
    cin >> n;
    vector<P> v(n);
    char c = 'A';
    for (auto& p : v) {
      p.first = c++;
      cin >> p.second;
    }
    sort(v.begin(), v.end(), [](const P& a, const P& b) { return a.second > b.second; });
    cout << "Case #" << k << ":";
    for (size_t i = 1; i < n; ++i) {
      bool found = false;
      do {
	found = false;
	for (size_t j = 0; j < i; ++j) {
	  if (v[j].second > v[i].second) {
	    cout << ' ' << v[j].first;
	    --v[j].second;
	    found = true;
	    //validate(v);
	  }
	}
      } while (found);
    }
    for (size_t i = 0; i < n-2; ++i) {
      while (v[i].second > 0) {
	cout << ' ' << v[i].first;
	--v[i].second;
	//validate(v);
      }
    }
    while (v[n-1].second > 0) {
      cout << ' ' << v[n-2].first << v[n-1].first;
      --v[n-1].second;
      --v[n-2].second;
      //validate(v);
    }
    cout << endl;
  }
}
