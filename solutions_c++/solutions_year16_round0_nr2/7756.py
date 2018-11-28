#include <iostream>
#include <cstdio>
#include <string>

#define DOWN '-'
#define UP '+'

using namespace std;

int main () {
  int N = -1;
  scanf("%d\n", &N);

  for (int i = 0; i < N; ++i) {
    string s;
    getline(cin, s);
    int count = 0;
    char curr = s[0];
    for (int j = 1; j < s.size(); ++j) {
      if (curr != s[j]) {
        count++;
        curr = s[j];
      }
    }
    if (s[s.size() - 1] == DOWN) count++;
    cout << "Case #" << (i + 1) << ": " << count << endl;
  }
  return 0;
}
