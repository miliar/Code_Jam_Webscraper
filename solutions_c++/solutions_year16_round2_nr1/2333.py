#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector<pair<string, int> > digs =
  { {"ZERO", 0}, {"XSI", 6}, {"GEIHT", 8 }, { "WTO", 2},
    {"UFOR", 4}, {"ONE", 1}, {"FIVE", 5},
    {"SEVEN", 7}, {"THREE", 3}, {"NINE", 9} };

int main() {
  size_t N;
  cin >> N;
  for (size_t k = 1; k <= N; ++k) {
    string str;
    cin >> str;
    //cerr << str << " : " << endl;
    vector<int> counts(256);
    for (unsigned char c : str) {
      ++counts[c];
    }
    string res;
    for (auto& p : digs) {
      auto& s = p.first;
      bool found;
      do {
	found = false;
	size_t i = 0;
	for (; i < s.size(); ++i) {
	  unsigned char c = s[i];
	  if (counts[c] > 0) {
	    --counts[c];
	  } else {
	    break;
	  }
	}
	if (i != s.size()) {
	  for (size_t j = 0; j < i; ++j) {
	    unsigned char c = s[j];
	    ++counts[c];
	  }
	} else {
	  res.push_back(p.second+'0');
	  found = true;
	}
      } while (found);
    }
    sort(res.begin(), res.end());
    cout << "Case #" << k << ": " << res << endl;
  }
}
