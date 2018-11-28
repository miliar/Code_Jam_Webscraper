#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

long long power (long long k, long long c) {
  long long result = 1;
  for (int i = 0; i < c; i++) {
    result *= k;
  }
//   cout << k << "^" << c << "=" << result << endl;
  return result;
}

int main () {
  long long t, k, c, s;
  cin >> t;
  for (int i = 0; i < t; i++) {
    cin >> k >> c >> s;
    cout << "Case #" << i + 1 << ": ";
    if (k > s) {
      cout << "IMPOSSIBLE\n";
      continue;
    }
//     cout << endl << "how many is there: " << power(k, c) << endl;
    long long sirka = (long long)( power(k, c-1) );
    long long stred = (sirka / 2);
    for (int j = 0; j < k; j++) {
      if (j != k-1) {
	cout << stred+1 << " ";
      } else {
	cout << stred+1 << endl;
      }
      stred += sirka;
    }
  }
  return 0;
}