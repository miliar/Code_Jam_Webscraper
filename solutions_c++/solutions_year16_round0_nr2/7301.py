#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

ifstream in("in.txt");

int main() {
  int t;
  string str;

  in >> t;

  for (int j = 0; j < t; j++) {
    in >> str;

    vector<bool> res;

    for (int i = 0; i < str.size(); i++) {
      if (str[i] == '-') {
        res.push_back(false);
      }
      else {
        res.push_back(true);
      }
    }

    while (res.size() > 0 && res.back()) {
      res.pop_back();
    }

    int counter = 0;

    while (res.size() > 0) {
      for (int i = 0; i < res.size(); i++) {
        res[i] = !res[i];
      }

      while (res.size() > 0 && res.back()) {
        res.pop_back();
      }

      counter++;
    }

    cout << "Case #" << j + 1 << ": " << counter << "\n";
  }

  return 0;
}
