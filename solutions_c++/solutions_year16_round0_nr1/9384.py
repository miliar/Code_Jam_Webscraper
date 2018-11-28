#include <iostream>
#include <vector>
#include <string>
using namespace std;
int main () {
  int t;
  cin >> t;

  for (int a = 0; a < t; a++) {
    long long n;
    cin >> n;

    if (n == 0) {
      cout << "Case #" << (a+1) << ": INSOMNIA" << endl;
      continue;
    }

    int orig = n;

    vector<bool> seen(10, false);

    int seen_c = 0;
    int iters = 0;
    while (seen_c != 10 && iters < 10000000) {
      string s = to_string(orig);

      for (int i = 0; i < s.size(); i++) {
        if (!seen[s[i] - '0']) {
          seen_c++;
          seen[s[i]-'0'] = true;
        }
      }

      orig += n;
      iters++;
    }

    orig -= n;

    if (iters == 10000000)
      cout << "Case #" << (a+1) << ": INSOMNIA" << endl;
    else
      cout << "Case #" << (a+1) << ": " << orig << endl;
  }

}