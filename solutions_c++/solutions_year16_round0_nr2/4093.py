#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

vector<string> next_states(const string& s) {
  vector<string> result;

  for (size_t i = 0; i < s.length(); ++i) {
    string str = s;
    reverse(str.begin(), str.begin()+i+1);
    for (size_t ii = 0; ii < i+1; ++ii) {
      str[ii] = (str[ii] == '-') ? '+' : '-';
    }
    result.push_back(str);
  }

  return result;
}

int solve(const string& s) {
  const string target(s.length(), '+');

  //cout << "target: " << target << endl;
  map<string, int> visited;
  visited[s] = 0;

  queue<string> frontier;
  frontier.push(s);

  while (!frontier.empty()) {
    string cur = frontier.front();
    frontier.pop();

    //cout << "cur: " << cur << endl;
    if (cur == target) return visited[cur];

    vector<string> next = next_states(cur);
    for (int j = 0; j < next.size(); ++j) {
      string n = next[j];
      if (visited.find(n) != visited.end()) {
        continue;
      }
      //cout << "next: " << n << endl;
      visited[n] = visited[cur] + 1;
      frontier.push(n);
    }
  }

  return 0;
}

int main(int argc, char* argv[]) {
  if (argc < 2) return 1;
  ifstream ifs(argv[1]);

  int t;
  ifs >> t;

  for (int i = 0; i < t; ++i) {
    string s;
    ifs >> s;
    cout << "Case #" << i+1 << ": " << solve(s) << endl;
  }

  return 0;
}
