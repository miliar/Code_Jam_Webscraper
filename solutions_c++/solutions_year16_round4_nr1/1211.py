#include <iostream>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

int T, N, counts[3];
char opts[] = { 'R', 'P', 'S' };
map<char, int> optIndex = {{ 'R', 0 }, { 'P', 1 }, { 'S', 2 }};
map<char, char> oppToWin = {{ 'R', 'S' }, { 'S', 'P' }, { 'P', 'R' }};

string buildString(string curr, int l) {
  if (l == 1) {
    sort(curr.begin(), curr.end());
    return curr;
  }
  string left = "";
  left += curr[0];
  left += oppToWin[curr[0]];
  string right = "";
  right += curr[1];
  right += oppToWin[curr[1]];
  string ll = buildString(left, l - 1);
  string rr = buildString(right, l - 1);
  if (ll + rr < rr + ll)
    return ll + rr;
  return rr + ll;
}

int main() {
  cin >> T;
  for (int t = 1; t <= T; t++) {
    cin >> N >> counts[0] >> counts[1] >> counts[2];
    string best = "";
    for (int i = 0; i < 3; i++) {
      for (int j = i + 1; j < 3; j++) {
        string start = "";
        start += opts[i];
        start += opts[j];
        string curr = buildString(start, N);
        int currCounts[] = {0, 0, 0};
        for (int k = 0; k < (int) curr.size(); k++) {
          currCounts[optIndex[curr[k]]]++;
        }
        bool valid = true;
        for (int k = 0; k < 3; k++) {
          if (currCounts[k] > counts[k]) {
            valid = false;
            break;
          }
        }
        if (valid && (curr < best || best == "")) {
          best = curr;
        }
      }
    }
    cout << "Case #" << t << ": ";
    if (best == "")
      cout << "IMPOSSIBLE" << endl;
    else
      cout << best << endl;
  }
}
