#include <iostream>
#include <cstdio>
#include <queue>

using namespace std;

int minute;
int D;
int P[1024];

int main() {
  freopen("/Users/corey.xpx/Desktop/B-large.in","r",stdin);
  freopen("/Users/corey.xpx/Desktop/out.txt","w",stdout);
  int T;
  int max_pancake = 0;
  cin >> T;
  for (int case_count = 1; case_count <= T; ++case_count) {
    max_pancake = 0;
    cin >> D;
    for (int i = 0; i < D; ++i) {
      cin >> P[i];
      max_pancake = max(max_pancake, P[i]);
    }
    minute = max_pancake;
    for (int i = 1; i < max_pancake; ++i) {
      int tmp_minute = i;
      for (int j = 0; j < D; j++) {
        if (P[j] > i) {
          tmp_minute += (P[j] + i - 1) / i - 1;
        }
      }
      if (tmp_minute < minute) {
        minute = tmp_minute;
      }
    }
    cout << "Case #" << case_count << ": " << minute << endl;
  }
  return 0;
}
