#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <tuple>
#include <string>
using namespace std;

typedef unsigned long long int llui;
typedef long long int lli;
typedef pair<int, int> pii;
typedef pair<string, string> pss;

const int sz = 1e5;
vector<pii> senators;

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";

    int n;
    cin >> n;
    senators.clear();
    for (int i = 0; i < n; ++i) {
      int a;
      cin >> a;
      senators.push_back(make_pair(a, i));
    }

    vector<char> c;

    while (true) {
      sort(senators.begin(), senators.end(), greater<pii>());
      if (senators[0].first == 1) {
        break;
      }
      if (senators[0].first == senators[1].first) {
        cout << (char)(senators[0].second + 'A') << (char)(senators[1].second + 'A') << " ";
        --senators[0].first;
        --senators[1].first;
      } else {
        cout << (char)(senators[0].second + 'A') << " "; 
        --senators[0].first;
      }
    }

    for (int i = 0; i < senators.size(); ++i) {
      if (senators[i].first == 1) {
        c.push_back(senators[i].second + 'A');
      }
    }
    if (c.size() % 2 == 1) {
      cout << c[c.size() - 1] << " ";
      c.pop_back();
    }

    for (int i = 0; i < c.size(); i += 2) {
      cout << c[i] << c[i + 1] << " ";
    }

    cout << endl;
  }
}

