#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

int main() {
  int T;
  cin >> T;
  for (int t=1; t<=T; ++t) {
    cout << "Case #" << t << ": ";
    int N;
    cin >> N;
    int senate[N];
    int total = 0;
    for (int n=0; n < N; ++n) {
      cin >> senate[n];
      total += senate[n];
    }
    while (total > 0) {

      int max_senate = *max_element(senate, senate+N);
      for (int j=0; j<N; ++j) {
        if (senate[j]==max_senate) {
          cout << alphabet[j];
          senate[j]--;
          total--;
          break;
        }
      }
      if (total == 0) {
        break;
      } else if (total != 2) {
        max_senate = *max_element(senate, senate+N);
        for (int j=0; j<N; ++j) {
          if (senate[j]==max_senate) {
            cout << alphabet[j];
            senate[j]--;
            total--;
            break;
          }
        }
      }
      cout << " ";
    }
    cout << endl;
  }
  return 0;
}
