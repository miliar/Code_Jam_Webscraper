#include <iostream>
#include <vector>

using namespace std;

int ctoi(char c) {
  return c - '0';
}

int solve(int n, const string &bs) {
  int total = 0;
  int invite = 0;

  for (int i = 0; i < bs.size(); i++) {
    if (total < i) {
      invite += (i - total);
      total = i;
    }

    total += ctoi(bs[i]);
  }

  return invite;
}

int main(int argc, char *argv[]) {
 
  int t;
  cin >> t;
  for (int i = 1; i <= t; i++) {
    int n;
    string bs;
    cin >> n >> bs;

    cout << "Case #" << i << ": " << solve(n, bs) << endl;
  }
}
