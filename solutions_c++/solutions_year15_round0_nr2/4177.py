#include <sstream>
#include <iostream>
#include <string>
#include <map>

using namespace std;

int case_count;

int f(const map<int, int> &house) {
  // for (auto it = house.begin(); it != house.end(); it++) {
  //   cout << "Debug: " << it->first << ": " << it->second << endl;
  // }
  int cur_max_key = next(house.end(), -1)->first;
  int cur_max_value = next(house.end(), -1)->second;
  int cur_min = cur_max_key;
  for (int i = 2; i <= cur_max_key / 2; i++) {
    map<int, int> h = house;
    if (cur_max_value == 1) {
      h.erase(next(h.end(), -1));
    } else {
      h[cur_max_key]--;
    }
    if (h.find(i) == h.end()) {
      h[i] = 1;
    } else {
      h[i]++;
    }
    if (h.find(cur_max_key - i) == h.end()) {
      h[cur_max_key - i] = 1;
    } else {
      h[cur_max_key - i]++;
    }

    cur_min = min(cur_min, f(h) + 1);
  }

  return cur_min;
}

void work(map<int, int> &house) {
  // for (auto it = house.begin(); it != house.end(); it++) {
  //   cout << it->first << ": " << it->second << endl;
  // }
  cout << "Case #" << case_count << ": " << f(house) << endl;
}

int main() {
  string line;
  int T;
  int read = 0;
  case_count = 0;
  getline(cin, line);
  istringstream iss_outer(line);
  iss_outer >> T;
  while (T-- > 0) {
    // Read s_max,
    int D;
    getline(cin, line);
    istringstream iss_inner1(line);
    iss_inner1 >> D;

    int p;
    map<int, int> house;

    getline(cin, line);
    istringstream iss_inner2(line);
    while (D-- > 0) {
      iss_inner2 >> p;
      auto search = house.find(p);
      if (search == house.end()) {
        house[p] = 1;
      } else {
        house[p]++;
      }
    }

    // Work on the data
    case_count++;
    work(house);
  }
  return 0;
}
