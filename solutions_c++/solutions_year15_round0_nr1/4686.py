#include <sstream>
#include <iostream>
#include <string>

using namespace std;

int case_count;

void work(const string &s) {
  int cur_max = 0;
  int sum = 0;
  for (int i = 0; i < s.size(); i++) {
    cur_max = max(cur_max, i - sum);
    sum += (s[i] - '0');
  }
  cout << "Case #" << case_count << ": " <<cur_max << endl;
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
    getline(cin, line);
    istringstream iss_inner1(line);
    int s_max;
    iss_inner1 >> s_max;
    string s;
    iss_inner1 >> s;

    // Work on the data
    case_count++;
    work(s);
  }
  return 0;
}
