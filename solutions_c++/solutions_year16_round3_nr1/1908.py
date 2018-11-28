#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <algorithm>
#include <map>

using namespace std;

int main() {
  int t;
  cin >> t;

  for (int i = 0; i < t; i++) {

    int n;
    cin >> n;
    vector<pair<int, char> > senators;
    for (int j = 0; j < n; j++) {
      int s;
      cin >> s;
      senators.push_back(make_pair(s, (char)j + 'A'));
    }

    cout << "Case #" << i + 1 << ": ";
    while (!senators.empty()) {
      sort(senators.begin(), senators.end(), greater<pair<int, char> >());

      if (senators.size() == 2) {
        if (senators[0].first == 1 || senators[1].first >= 2) {
          cout << senators[0].second << senators[1].second << " ";
          senators[0].first--;
          senators[1].first--;
        } else if (senators[0].first > 2) {
          cout << senators[0].second << senators[0].second << " ";
          senators[0].first -= 2;
        } else {
          cout << senators[0].second << " ";
          senators[0].first--;
        }
      } else {
        if (senators[0].first > senators[1].first) {
          cout << senators[0].second << senators[0].second << " ";
          senators[0].first -= 2;
        } else if (senators.size() > 3 || senators[0].first > 1) {
          cout << senators[0].second << senators[1].second << " ";
          senators[0].first--;
          senators[1].first--;
        } else {
          cout << senators[0].second << " ";
          senators[0].first--;
        }
      }

      for (int j = senators.size() - 1; j >= 0; j--) {
        if (senators[j].first <= 0) {
          senators.erase(senators.begin() + j);
        }
      }
    }

    cout << endl;
  }

  return 0;
}

