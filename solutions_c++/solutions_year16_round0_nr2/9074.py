#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <functional>

using namespace std;

char flip(char c) {
  if (c == '+') {
    return '-';
  }
  return '+';
}

void flip(int start, string& line) {
  for (int i = 0; i <= start; ++i) {
    line[i] = flip(line[i]);
  }
  for (int i = start, j = 0; i > j; --i, ++j) {
    char temp = line[i];
    line[i] = line[j];
    line[j] = temp;
  }
}

int main()
{
  int T;
  cin >> T;

  for (int t = 0; t < T; ++t)
  {
    string line;
    cin >> line;
    int flips = 0;
    for (int i = line.size()-1 ; i >= 0; --i) {
      if (line.at(i) == '+') { continue; }
      if (i > 0 && line.at(0) == '+') {
        int j = 0;
        while (j < i-1 && line[j+1] == '+') {
          ++j;
        }
        flip(j, line);
        flips++;
      }
      flip(i, line);
      flips++;
    }
    cout << "Case #" << t + 1 << ": " << flips;
    cout << endl;
  }
  return 0;
}