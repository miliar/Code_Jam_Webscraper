#include <cstdlib>
#include <string>
#include <iostream>
#include <set>

using namespace std;

int main() {
  // Number of cases.
  string dump;
  int N;
  cin >> N;
  getline(cin, dump);

  // For each test case.
  for (int i=1; i<=N; i++) {
    string input;
    getline(cin, input);

    int n = input.size();
    int flip = 0;
    int p;

    for (p=n-1; p>=0 && input[p] == '+'; p--);
    if (p < 0) goto done;
    n = p+1;

    for (p=0; p<n && input[p] == '-'; p++);
    if (p > 0)
      flip++;

    while (p < n) {
      for (; p<n && input[p] == '+'; p++);
      for (; p<n && input[p] == '-'; p++);
      flip+=2;
    }

  done:
    cout << "Case #" << i << ": " << flip << endl;
  }

  return 0;
}
