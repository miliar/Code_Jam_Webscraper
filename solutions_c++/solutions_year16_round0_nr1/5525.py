#include <iostream>
#include <vector>
using namespace std;

int main() {
  int T;
  cin >> T;

  for (int t = 1; t <= T; ++t) {
    long long N;
    cin >> N;

    if (N == 0) {
      cout << "Case #" << t << ": INSOMNIA" << endl;
      continue;
    }

    int checked = 0;
    vector<bool> check = vector<bool>(10, false);

    int i = 1;
    while (true) {
      long long sheep = N * i;
      while (sheep != 0) {
	int digit = sheep % 10;
	if (check[digit] == false) {
	  check[digit] = true;
	  checked++;
	  if (checked == 10) {
	    cout << "Case #" << t << ": " << N * i << endl;
	    break;
	  }
	}
	sheep /= 10;
      }
      if (checked == 10) break;
      ++i;
    }
  }
  return 0;
}
