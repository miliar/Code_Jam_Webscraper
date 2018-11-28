#include <algorithm>
#include <array>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <list>
#include <map>
#include <set>
#include <vector>
#include <math.h>

using namespace std;

void run(int t) {
  int N; cin >> N;
  vector<string> input;
  vector<int> p(N, 0);  // pointers
  for (int i = 0; i < N; i++) {
    string s; cin >> s;
    input.push_back(s);
  }
  list<vector<int>> compressed;
  int finished = 0;
  while (finished == 0) {
    compressed.push_back(vector<int>(N, 0));
    char id;
    for (int i = 0; i < N; i++) {
      char curr = input[i][p[i]];
      if (i == 0) id = curr;
      if (id != curr) {
        cout << "Case #" << t << ": Fegla Won" << endl;
        return;
      }
      int count = 0;
      while (p[i] < input[i].size() && curr == input[i][p[i]]) {
        count++;
        p[i]++;
      }
      compressed.back()[i] = count;
      if (p[i] == input[i].size()) finished++;
    }
    if (finished > 0 && finished != N) {
      cout << "Case #" << t << ": Fegla Won" << endl;
      return;
    }
  }
  int result = 0;
  for (vector<int> row : compressed) {
    int sum = 0;
    for (int i = 0; i < N; i++) sum += row[i];
    int avg = (int)round(((double)sum) / N);
    for (int i = 0; i < N; i++) result += abs(row[i] - avg);
  }
  cout << "Case #" << t << ": " << result << endl;
}

int main() {
  cout << setprecision(7) << fixed;
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    run(t);
  }
}
