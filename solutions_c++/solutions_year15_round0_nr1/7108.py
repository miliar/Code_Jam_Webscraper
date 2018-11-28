#include <iostream>
#include <cstdio>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int get_minimum_ovation(int n, const string& audience) {
  int claps = 0;
  int result = 0;
  for (int i = 0; i <= n; i++) {
    if (claps >= i) {
      claps += audience.at(i) - '0';
    } else {
      int diff = i - claps;
      result += diff;
      claps += diff + audience.at(i) - '0';
    }
  }
  return result;
}

vector<string> split(const string& input, char delim)
{
    istringstream stream(input);

    string field;
    vector<string> result;
    while (getline(stream, field, delim)) {
        result.push_back(field);
    }
    return result;
}

int main() {
  string line;
  int m = 0;
  int n = 0;
  string audience;

  getline(cin, line);
  m = atoi(line.c_str());

  vector<string> lines(m);
  for (int i = 0; i < m; i++) {
    string l;
    getline(cin, l);
    lines[i] = l;
  }
  
  for (int i = 0; i < lines.size(); i++) {
    line = lines.at(i);
    auto splitted = split(line, ' ');
    int n = atoi(splitted.at(0).c_str());
    audience = splitted.at(1);
    cout << "Case #" << i + 1 << ": " << get_minimum_ovation(n, audience) << endl;
  }
}
