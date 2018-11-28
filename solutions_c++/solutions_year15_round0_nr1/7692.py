#include <iostream>
#include <string>
#include <vector>
using namespace std;

// To execute C++, please define "int main()"

int main() {
  int T;
  cin >> T;
  vector<int> counts;
  vector<string> strings;
  for (int i = 0; i < T; i++) {
    int s;
    string tmp;
    cin >> s >> tmp;
    counts.push_back(s);
    strings.push_back(tmp);
  }
  for (int i = 0; i < T; i++) {
    int num = 0;
    int curr = 0;
    string tmp = strings[i]; 
    for (int j = 0; j <= counts[i]; j++) {
      int value = tmp[j] - '0'; 
      if (j == 0) {
        curr += value;
      } else {
        if (curr >= j) {
          curr += value;
        } else {
          num += (j - curr);
          curr = j + value;
        }
      }
    }
    cout << "Case #" << i+1 << ": " << num << endl;
  }
  return 0;
}
